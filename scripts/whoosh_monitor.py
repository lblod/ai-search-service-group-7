from pathlib import Path

from whoosh.index import open_dir

DATA_DIR = Path(__file__).parent.parent / 'data'
INDEX_DIR = DATA_DIR / 'index'

INDEX = open_dir(INDEX_DIR)

print(f'whoosh index lives in: {INDEX_DIR}')
print(f'  - number of documents: {INDEX.doc_count()}')
print(f'  - schema: {INDEX.schema}')
