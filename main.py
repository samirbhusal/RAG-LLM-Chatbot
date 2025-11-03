from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the key securely from environment variables
api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages(
    ("You are a world class RAG chatbot developer for customer support.","{input}")
)

output_parser = StrOutputParser()

chains = prompt | llm | output_parser


response = chains.invoke({"input": "how can langsmith help with building chatbot?"})
print(response)

