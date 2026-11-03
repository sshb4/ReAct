"""Build a tagged, selectable PDF from report/report.md and render it for review.

Optional artifact dependencies: reportlab, pypdf, pymupdf, pillow.
These are independent of the application environment and lockfile.
"""
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (ArrayObject, BooleanObject, DictionaryObject,
                           NameObject, NumberObject, TextStringObject)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output' / 'pdf'
TEMP = ROOT / 'tmp' / 'pdfs'
REPO = 'https://github.com/sshb4/ReAct'


def obj(values):
    return DictionaryObject({NameObject(k): v for k, v in values.items()})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    TEMP.mkdir(parents=True, exist_ok=True)
    regular, bold = 'Helvetica', 'Helvetica-Bold'
    font = Path('/System/Library/Fonts/Supplemental/Arial.ttf')
    if font.exists():
        pdfmetrics.registerFont(TTFont('Report', str(font)))
        pdfmetrics.registerFont(TTFont('ReportBold', str(font.with_name('Arial Bold.ttf'))))
        regular, bold = 'Report', 'ReportBold'
    c = canvas.Canvas(str(TEMP / 'raw.pdf'), pagesize=letter, pageCompression=1)
    tags, counts = [], {}
    y = 747

    @contextmanager
    def tag(kind):
        page = c.getPageNumber() - 1
        mcid = counts.get(page, 0)
        counts[page] = mcid + 1
        tags.append((page, mcid, kind))
        c.addLiteral(f'/{kind} <</MCID {mcid}>> BDC')
        yield
        c.addLiteral('EMC')

    def footer():
        c.addLiteral('/Artifact BMC')
        c.setStrokeColor(HexColor('#CFD8E2'))
        c.line(44, 39, 568, 39)
        c.setFillColor(HexColor('#536274'))
        c.setFont(regular, 8)
        c.drawString(44, 25, 'Sasha Bates | U0-HW-09 | November 3, 2026')
        c.drawRightString(568, 25, str(c.getPageNumber()))
        c.addLiteral('EMC')

    def next_page():
        nonlocal y
        footer()
        c.showPage()
        y = 747

    def paragraph(value, kind='P'):
        nonlocal y
        size = {'H1': 20, 'H2': 12.5, 'P': 10.2}[kind]
        face = bold if kind.startswith('H') else regular
        lines = simpleSplit(value, face, size, 524)
        leading = size * 1.35
        # Keep headings with the start of their following paragraph.
        required = len(lines) * leading + (35 if kind.startswith('H') else 0)
        if y - required < 55:
            next_page()
        with tag(kind):
            c.setFont(face, size)
            c.setFillColor(HexColor('#205C8A' if kind.startswith('H') else '#17263A'))
            for line in lines:
                if y < 55:
                    raise ValueError('Paragraph is too long for one page')
                c.drawString(44, y, line)
                y -= leading
        y -= 8 if kind == 'P' else 9

    source = (ROOT / 'report' / 'report.md').read_text()
    for block in source.strip().split('\n\n'):
        block = block.strip()
        if block == '---':
            next_page()
        elif block.startswith('# '):
            paragraph(block[2:], 'H1')
        elif block.startswith('## '):
            paragraph(block[3:], 'H2')
        elif block.startswith('- '):
            # Each disclosure bullet is its own tagged paragraph in reading order.
            for line in block.splitlines():
                paragraph(line)
        else:
            paragraph(' '.join(block.splitlines()))
    footer()
    c.save()

    writer = PdfWriter()
    writer.append(PdfReader(TEMP / 'raw.pdf'))
    structure = obj({'/Type': NameObject('/StructTreeRoot')})
    sr = writer._add_object(structure)
    document = obj({'/Type': NameObject('/StructElem'), '/S': NameObject('/Document'),
                    '/P': sr, '/K': ArrayObject()})
    dr = writer._add_object(document)
    parents = {page: [] for page in counts}
    for page, mcid, kind in tags:
        element = obj({'/Type': NameObject('/StructElem'), '/S': NameObject('/' + kind),
                       '/P': dr, '/Pg': writer.pages[page].indirect_reference,
                       '/K': NumberObject(mcid)})
        ref = writer._add_object(element)
        document['/K'].append(ref)
        parents[page].append(ref)
    nums = ArrayObject()
    for page, refs in parents.items():
        nums.extend([NumberObject(page), ArrayObject(refs)])
        writer.pages[page][NameObject('/StructParents')] = NumberObject(page)
        writer.pages[page][NameObject('/Tabs')] = NameObject('/S')
    structure.update({NameObject('/K'): ArrayObject([dr]),
                      NameObject('/ParentTree'): writer._add_object(obj({'/Nums': nums})),
                      NameObject('/ParentTreeNextKey'): NumberObject(len(parents))})
    writer._root_object.update({NameObject('/StructTreeRoot'): sr,
                                NameObject('/MarkInfo'): obj({'/Marked': BooleanObject(True)}),
                                NameObject('/Lang'): TextStringObject('en-US'),
                                NameObject('/ViewerPreferences'): obj({'/DisplayDocTitle': BooleanObject(True)})})
    writer.add_metadata({'/Title': 'ReAct Agent with Vector Retrieval', '/Author': 'Sasha Bates',
                         '/Subject': 'U0-HW-09 design, recorded outcomes and limitations'})
    final = OUT / 'bates-sasha-vector-retrieval.pdf'
    writer.write(final)

    import pymupdf
    reader = PdfReader(final)
    text = '\n'.join(p.extract_text() for p in reader.pages)
    assert REPO in text and all(f'Q{i}:' in text for i in range(1, 10))
    assert 'AI-assistance disclosure' in text
    doc = pymupdf.open(final)
    for i, page in enumerate(doc):
        page.get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(TEMP / f'page-{i + 1}.png')
        for block in page.get_text('blocks'):
            assert 0 <= block[0] <= block[2] <= 613 and 0 <= block[1] <= block[3] <= 793
    evidence = {'pages': len(reader.pages), 'pdf_sha256': hashlib.sha256(final.read_bytes()).hexdigest(),
                'selectable_text': True, 'semantic_headings': True, 'logical_reading_order': True,
                'language': 'en-US', 'data_tables': False, 'visual_review': 'pending',
                'pdf_ua_certified': False}
    (ROOT / 'report' / 'accessibility-check.json').write_text(json.dumps(evidence, indent=2) + '\n')
    print(final)
    print(json.dumps(evidence, indent=2))


if __name__ == '__main__':
    main()
