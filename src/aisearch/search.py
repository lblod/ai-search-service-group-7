from pathlib import Path

from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser

from aisearch.schema import ALL_SEARCH_FIELDS

DATA_DIR = Path('/home/peter/data')
INDEX_DIR = DATA_DIR / 'index'
INDEX = open_dir(INDEX_DIR)

PARSER = MultifieldParser(ALL_SEARCH_FIELDS, INDEX.schema)


def search(query: str):
    query = PARSER.parse(query)
    print(query)

    with INDEX.searcher() as searcher:
        results = searcher.search(query)
        return results


if __name__ == '__main__':
    queries = ['location:leuven', 'voorlopig_rijbewijs AND location:aarschot']

    for query in queries:
        results = search(query=query)
        print('-' * 50)
        print(f'Question: {query}')
        print(f'Results:\n{results}')
        print('-' * 50)
