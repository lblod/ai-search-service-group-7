from pathlib import Path

from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser

from aisearch.schema import ALL_SEARCH_FIELDS

DATA_DIR = Path(__file__).parent.parent.parent / 'data'
INDEX_DIR = DATA_DIR / 'index'
INDEX = open_dir(INDEX_DIR)

PARSER = MultifieldParser(ALL_SEARCH_FIELDS, INDEX.schema)


def search(query: str, limit: int = 10):
    query = PARSER.parse(query)

    with INDEX.searcher() as searcher:
        results = searcher.search(query, limit=limit)

        results_data = []
        for result in results:
            data = dict(result.items())
            data.update({'score': result.score})
            results_data.append(data)

        return results_data


if __name__ == '__main__':
    queries = ['location:leuven', '"voorlopig rijbewijs" AND location:aarschot']

    for query in queries:
        results = search(query=query)
        print('-' * 50)
        print(f'Question: {query}')
        print(f'Results ({len(results)}):\n{results}')
        print('-' * 50)
