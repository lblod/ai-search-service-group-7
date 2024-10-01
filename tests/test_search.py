from aisearch.search import search


def test_search():
    query = 'location:leuven'
    results = search(query=query, limit=20)
    assert len(results) == 20

    query = '"voorlopig rijbewijs" AND location:aarschot'
    results = search(query=query, limit=20)
    assert len(results) == 2
