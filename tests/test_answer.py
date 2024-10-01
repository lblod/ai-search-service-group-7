from aisearch.answer import answer
from aisearch.search import search


def test_answer():
    query = '"voorlopig rijbewijs" AND location:aarschot'
    results = search(query=query)
    response = answer(
        question='hoe lang is een voorlopig rijbewijs geldig?', results_data=results
    )
    # right answer is : Een voorlopig rijbewijs is 18 maanden of 36 maanden geldig.
    assert '18 maand' in response
    assert '36 maand' in response
