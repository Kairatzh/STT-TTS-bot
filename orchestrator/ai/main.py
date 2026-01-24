from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from ai.prompt import prompt_text

from dotenv import load_dotenv
import os

load_dotenv()

prompt_template = PromptTemplate(
    template=prompt_text,
    input_variables=["text"]
)

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_KEY"),
    temperature=0.8,
    max_tokens=40
)

output_parser = StrOutputParser()

chain = prompt_template | llm | output_parser

def generate(text: str):
    return chain.invoke({"text": text})    

