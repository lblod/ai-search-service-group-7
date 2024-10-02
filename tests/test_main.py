from aisearch.main import perform_ai_search


def test_perform_ai_search():
    question = 'hoeveel kost een voorlopig rijbewijs in aarschot'
    answer, sources, query = perform_ai_search(question=question)
    assert 'location:aarschot' in query
    assert len(sources) > 0
    assert '25' in answer
