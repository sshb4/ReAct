"""Small real-service checks, separate from the nine required-query results."""
import json
import math
from pathlib import Path

from app.agent import Action
from app.ask import SYSTEM
from app.config import PROJECT_DIR, RUNTIME_PROFILE, runtime_metadata
from app.local import OllamaEmbeddings, build_local_model, local_model_inventory


def main():
    if RUNTIME_PROFILE != 'local':
        raise SystemExit('Select local mode with HW09_ENV_FILE=.env.local')
    models = local_model_inventory()
    print('Installed model tags:', ', '.join(m['name'] for m in models), flush=True)
    vector = OllamaEmbeddings().embed_query('What should happen when a food employee vomits?')
    norm = math.sqrt(sum(v * v for v in vector))
    if norm < 0.01:
        raise ValueError('Embedding vector norm is too small')
    print(f'Real embedding OK: {len(vector)} dimensions; norm={norm:.5f}', flush=True)
    prompt = SYSTEM + '\nNo source passages have been retrieved in this smoke check. Return insufficient_evidence.'
    raw = build_local_model(prompt)([{'role': 'user', 'content': 'What do the unavailable documents say?'}])
    action = Action.model_validate_json(raw)
    print('Real structured chat action:', action.kind, flush=True)
    output = PROJECT_DIR / '.runtime' / 'local-smoke.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps({**runtime_metadata(), 'local_models': models,
                                  'embedding_dimensions': len(vector), 'embedding_norm': norm,
                                  'chat_action': action.model_dump()}, indent=2) + '\n')


if __name__ == '__main__':
    main()
