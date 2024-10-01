from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from aisearch.prompts import QUESTION_TO_QUERY_PROMPT
from aisearch.schema import CATALOG_SCHEMA_DESCRIPTIONS

# setup the llm model
MODEL = OllamaLLM(model='mistral', temperature=0.0, max_tokens=512)
PROMPT = PromptTemplate(
    template=QUESTION_TO_QUERY_PROMPT,
    input_variables=['question'],
    partial_variables={'schema': CATALOG_SCHEMA_DESCRIPTIONS},
)


def question_to_query(question: str) -> str:
    chain = PROMPT | MODEL
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
