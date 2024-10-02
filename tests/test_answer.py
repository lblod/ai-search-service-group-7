from aisearch.answer import answer_question
from aisearch.search import search_for_products


def test_answer():
    query = '"voorlopig rijbewijs" AND location:aarschot'
    results = search_for_products(query=query)
    response = answer_question(
        question='hoe lang is een voorlopig rijbewijs geldig?', results_data=results
    )
    # right answer is : Een voorlopig rijbewijs is 18 maanden of 36 maanden geldig.
    print(response)
    assert '18 maand' in response
    assert '36 maand' in response
