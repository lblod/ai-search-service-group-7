from aisearch.question import question_to_query


def test_question_to_query():
    question = 'ik wil een marktplaats in leuven'
    query = question_to_query(question=question)
    assert 'markt' in query
    assert 'AND' in query
    assert 'location:leuven' in query

    question = 'ik heb een voorlopig rijbewijs nodig in aarschot'
    query = question_to_query(question=question)
    assert '"voorlopig rijbewijs"' in query
    assert 'AND' in query
    assert 'location:aarschot' in query
