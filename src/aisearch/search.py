import os
from pathlib import Path

from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser

from aisearch.schema import ALL_SEARCH_FIELDS, SCORE_KEY

INDEX_DIR = Path(os.environ.get('WHOOSH_INDEX_PATH', '/data/index'))
INDEX = open_dir(INDEX_DIR)

PARSER = MultifieldParser(ALL_SEARCH_FIELDS, INDEX.schema)


def search_for_products(query: str, limit: int = 10):
    query = PARSER.parse(query)

    with INDEX.searcher() as searcher:
        results = searcher.search(query, limit=limit)

        results_data = []
        for result in results:
            data = dict(result.items())
            data.update({SCORE_KEY: result.score})
            results_data.append(data)

        return results_data


if __name__ == '__main__':
    queries = ['location:leuven', '"voorlopig rijbewijs" AND location:aarschot']

    for query in queries:
        results = search_for_products(query=query)
        print('-' * 50)
        print(f'Question: {query}')
        print(f'Results ({len(results)}):\n{results}')
        print('-' * 50)
