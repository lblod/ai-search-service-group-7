from aisearch.answer import answer
from aisearch.search import search


def test_answer():
    query = '"voorlopig rijbewijs" AND location:aarschot'
    results = search(query=query)
    response = answer(
        question='hoe lang is een voorlopig rijbewijs geldig?', results_data=results
    )

    print(response)
