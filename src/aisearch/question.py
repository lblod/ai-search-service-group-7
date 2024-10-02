from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from aisearch.prompts import QUESTION_TO_QUERY_PROMPT
from aisearch.schema import CATALOG_SCHEMA_DESCRIPTIONS
from aisearch.cfg import OLLAMA_ENDPOINT


def question_to_query(question: str) -> str:
    model = OllamaLLM(model='mistral', temperature=0.0, max_tokens=512, base_url=OLLAMA_ENDPOINT)
    prompt = PromptTemplate(
        template=QUESTION_TO_QUERY_PROMPT,
        input_variables=['question'],
        partial_variables={'schema': CATALOG_SCHEMA_DESCRIPTIONS},
    )
    chain = prompt | model
    return chain.invoke({'question': question})


if __name__ == '__main__':
    questions = [
        'ik wil een marktplaats in leuven',
        'ik heb een voorlopig rijbewijs nodig in aarschot',
    ]

    for question in questions:
        query = question_to_query(question=question)
        print('-' * 50)
        print(f'Question: {question}')
        print(f'Query: {query}')
        print('-' * 50)
