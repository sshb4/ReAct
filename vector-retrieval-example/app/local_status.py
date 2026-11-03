"""Inspect local pipeline progress without contacting a model service."""
import json
from app.config import PROJECT_DIR


def main():
    import chromadb
    from chromadb.config import Settings
    status = {}
    pipeline = PROJECT_DIR / '.runtime' / 'local-pipeline-state.json'
    if pipeline.exists():
        status['pipeline'] = json.loads(pipeline.read_text())
    database = PROJECT_DIR / 'chroma_local'
    if (database / 'chroma.sqlite3').exists():
        client = chromadb.PersistentClient(path=str(database), settings=Settings(anonymized_telemetry=False))
        try:
            status['indexed_chunks'] = client.get_collection('hw09_documents_local').count()
        except Exception as error:
            status['index_status'] = type(error).__name__
    else:
        status['indexed_chunks'] = 0
    results = PROJECT_DIR / 'results-local'
    outcomes = []
    for path in sorted(results.glob('Q*.json')):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        outcomes.append({'query_id': data.get('query_id', path.stem),
                         'terminal_reason': data['terminal_reason'], 'steps': data['steps']})
    status['recorded_query_outcomes'] = outcomes
    manifest = PROJECT_DIR / 'manifest.local.json' 
    status['complete_manifest_present'] = manifest.exists()
    print(json.dumps(status, indent=2))


if __name__ == '__main__':
    main()
