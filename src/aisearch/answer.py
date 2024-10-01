from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from aisearch.prompts import QUESTION_ANSWERING_PROMPT


def answer(question: str, results_data: list[dict]) -> str:
    model = OllamaLLM(model='mistral', temperature=0.0, max_tokens=512)
    prompt = PromptTemplate(
        template=QUESTION_ANSWERING_PROMPT,
        input_variables=['documents', 'question'],
    )
    chain = prompt | model
    return chain.invoke({'documents': str(results_data), 'question': question})
