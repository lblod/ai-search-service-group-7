from aisearch.search import search_for_products


def test_search():
    query = 'location:leuven'
    results = search_for_products(query=query, result_limit=20)
    assert len(results) == 20

    query = '"voorlopig rijbewijs" AND location:aarschot'
    results = search_for_products(query=query, result_limit=20)
    assert len(results) == 2
