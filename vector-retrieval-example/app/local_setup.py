"""Download the required local embedding model with bounded progress output."""
import argparse
import json
import shutil
import urllib.request

from app.config import PROJECT_DIR
from app.local import NoRedirect, local_base_url, local_request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', choices=('qwen3-embedding:8b', 'qwen3:4b'), default='qwen3-embedding:8b')
    args = parser.parse_args()
    installed = {m.get('name') for m in local_request('/api/tags').get('models', [])}
    if args.model in installed:
        print(args.model + ' is already installed', flush=True)
        return
    from pathlib import Path
    volume = Path.home() / '.ollama' / 'models'
    free = shutil.disk_usage(volume if volume.exists() else PROJECT_DIR).free
    minimum_gib = 7 if args.model == 'qwen3-embedding:8b' else 5
    if free < minimum_gib * 1024**3:
        raise SystemExit(f'Free at least {minimum_gib} GiB on the model-storage volume before downloading.')
    payload = {'model': args.model, 'stream': True}
    request = urllib.request.Request(local_base_url() + '/api/pull', data=json.dumps(payload).encode(),
                                     headers={'Content-Type': 'application/json'})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    previous = None
    status = ''
    with opener.open(request, timeout=180) as response:
        for line in response:
            event = json.loads(line)
            if event.get('error'):
                raise RuntimeError(event['error'])
            total = event.get('total', 0)
            bucket = int(10 * event.get('completed', 0) / total) if total else None
            status = event.get('status', '')
            marker = (status, bucket)
            if marker != previous:
                print(status + (f' {bucket * 10}%' if bucket is not None else ''), flush=True)
                previous = marker
    if status != 'success':
        raise RuntimeError('Download ended without a success event')


if __name__ == '__main__':
    main()
