from aisearch.answer import answer_question
from aisearch.question import question_to_query
from aisearch.schema import LOCATION_KEY, PRODUCT_NAME_KEY, SCORE_KEY, TARGET_GROUP, URL
from aisearch.search import search_for_products

NO_RESULTS_ANSWER = """Er werd niks gevonden op basis van uw vraag.
Probeer uw vraag te herformuleren"""

SOURCES_KEYS = [PRODUCT_NAME_KEY, LOCATION_KEY, TARGET_GROUP, URL, SCORE_KEY]


def perform_ai_search(
    question: str, result_limit: int = 5
) -> tuple[str, list[dict], str]:
    # translate question to whoosh query
    query = question_to_query(question=question)
    # perform the query and get results back
    search_results = search_for_products(query=query, result_limit=result_limit)

    # deal with no results found case
    if not search_results:
        return NO_RESULTS_ANSWER, [], query

    # generate answer based on results and question
    answer = answer_question(question=question, results_data=search_results)

    # filter search results
    sources = []
    for result in search_results:
        source = {k: result[k] for k in SOURCES_KEYS}
        sources.append(source)

    return answer, sources, query
