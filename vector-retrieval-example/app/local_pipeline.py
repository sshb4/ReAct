"""Wait for the local index, then record all nine queries without manual handoff."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

from app.config import DEFAULT_MANIFEST_PATH, PROJECT_DIR, RUNTIME_PROFILE


def index_complete(path: Path) -> bool:
    try:
        data = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    return (data.get('runtime_profile') == 'local'
            and data.get('physical_page_count') == 1110
            and data.get('ingested_chunk_count', 0) > 0
            and data.get('record_count') == data.get('ingested_chunk_count'))


def main():
    if RUNTIME_PROFILE != 'local':
        raise SystemExit('Select HW09_ENV_FILE=.env.local')
    runtime = PROJECT_DIR / '.runtime'
    runtime.mkdir(exist_ok=True)
    state_path = runtime / 'local-pipeline-state.json'
    log_path = runtime / 'local-pipeline.log'

    def state(stage, **extra):
        value = {'stage': stage, 'updated_at': datetime.now(timezone.utc).isoformat(), **extra}
        temporary = state_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(value, indent=2) + '\n')
        temporary.replace(state_path)

    with log_path.open('a', buffering=1) as log:
        def announce(message):
            print(message, flush=True)
            print(datetime.now(timezone.utc).isoformat(), message, file=log, flush=True)

        try:
            state('waiting_for_index')
            announce('Waiting for the full local index; Golem credentials are not used.')
            deadline = time.monotonic() + 6 * 60 * 60
            while not index_complete(DEFAULT_MANIFEST_PATH):
                if time.monotonic() > deadline:
                    raise TimeoutError('Index was not completed within six hours; inspect ingestion before retrying')
                time.sleep(10)
            state('running_required_queries', semantic_review='pending')
            announce('Index complete. Starting Q1-Q9 with k=6, max_steps=16.')
            command = [sys.executable, '-u', '-m', 'app.required', '--k', '6', '--max-steps', '16']
            with subprocess.Popen(command, cwd=PROJECT_DIR, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True, bufsize=1) as process:
                for line in process.stdout:
                    announce(line.rstrip())
                code = process.wait()
            if code:
                raise RuntimeError(f'Required-query runner exited with status {code}; see {log_path.name}')
            summary = json.loads((PROJECT_DIR / 'results-local' / 'summary.json').read_text())
            state('queries_recorded', semantic_review='pending', outcomes=summary)
            announce('All nine results recorded. Claim-by-claim evidence review is still required.')
        except Exception as error:
            state('error', message=f'{type(error).__name__}: {error}')
            announce(f'{type(error).__name__}: {error}')
            raise


if __name__ == '__main__':
    main()
