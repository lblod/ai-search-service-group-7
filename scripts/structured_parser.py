# this file shows how we can use a pydantic model output parser to
from typing import Optional

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from pydantic import BaseModel, Field

# prompt template with 2 parameters that will be filled later
# format_instructions will contain instructions based on the pydantic model definition
# input_text is the input that will be used to extract the data from
prompt = """You are an AI-assistant that extracts structured data from service information pages of the flemish government.
You follow the output structure defined below:
{format_instructions}

Provide only the json-output as answer.

Service information text:
{input_text}
"""

# setup the llm model
model = OllamaLLM(model='mistral', temperature=0.0, max_tokens=512)


# pydantic model that defines the structured output in terms of members, types and
# descriptions that will be used to extract the data from the input text
class DecisionExtractor(BaseModel):
    cost: Optional[float] = Field(description='Cost of the service in euros.')
    service_name: str = Field(description='The name/title of the service.')


# setup the parser based on the pydantic model
parser = PydanticOutputParser(pydantic_object=DecisionExtractor)


# define the prompt template and partially fill in the template with the
# pydantic model parser instructions
system_prompt = PromptTemplate(
    template=prompt,
    input_variables=['input_text'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

# setup the chain to execute
# - first, fill in the input text in the prompt
# - next, call the model with the system prompt
# - finally, parse the model response and map it to the pydantic model
chain = system_prompt | model | parser


#####
# invoking the actual chain with input data

input_text = """
Voorlopig rijbewijs
Van toepassing in Pelt
Een voorlopig rijbewijs geeft je de toelating om met een voertuig op de openbare weg te rijden als voorbereiding op het praktisch rijexamen. Je moet minstens 5 maanden oefenen met je voorlopig rijbewijs.

Kost
Kostprijs
20 euro te betalen bij de aanvraag of bij het afhalen wanneer je het voorlopig rijbewijs online hebt aangevraagd.
"""

# response will be of type DecisionExtractor
response = chain.invoke({'input_text': input_text})


print(response)
print(type(response))
