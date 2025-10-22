from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from Assignment_matcher.openai_embedding import vector_store
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
import re

load_dotenv()

model = ChatOpenAI()

retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs={
        "k" : 2
    }
)

query = """The Word Search challenge involves checking if a specific word can be found within a 2D grid of characters, where the grid has dimensions m by n. Your task is to verify whether the given word exists somewhere in the board.
"""

prompt = PromptTemplate(
    template="""
    You are a plagiarism detector for academic assignments.
    I will provide you with a piece of text. Your task is to:
    Search through stored academic assignment chunks.
    Find the most similar or most copied text.
    Return only the closest matching content from the database.
    Be accurate. Match even if the wording is slightly changed but the context is the same.
    Text to check:
    {user_input}
    """,
    input_variables=["user_input"]
)

def format_docs(raw_data):
    raw_data = ' '.join([doc.page_content for doc in raw_data])  # join all list items into one string
    
    context_text = raw_data.replace('\r', '').replace('\n', ' ')
    context_text = re.sub(r'\s+', ' ', context_text).strip()

    return context_text

parser = StrOutputParser()

chain = retriever | RunnableLambda(format_docs) | model | parser

result = chain.invoke(query)

print(result)

