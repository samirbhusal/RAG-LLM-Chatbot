from itertools import chain

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
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

chains = prompt | llm

response = chains.invoke({"input": "how can langsmith help with building chatbot?"})
print(response.content)

# response = llm.invoke("How Can I build customer support RAG Chatbot?")
# print(response.content)

