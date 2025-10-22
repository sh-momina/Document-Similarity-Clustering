from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from split_data import splited_data

import numpy as np


def get_embedding(text):
    model = OpenAIEmbeddings(model="text-embedding-3-small")  
    embedding = model.embed_query(text)  
    return embedding

load_dotenv()

# print(splited_data)

vector_final = []

for doc_chunks in splited_data:
    chunk_embeddings = []
    for chunk in doc_chunks:
        # print("\n",chunk,"\n")
        emb = get_embedding(chunk)  
        # print("\n",len(emb),"\n")
        chunk_embeddings.append(emb)
        
    avg_emb = np.array(chunk_embeddings)
    # print("\n",avg_emb.shape,"\n")
    vector_final.append(avg_emb.flatten())

vector_final = np.array(vector_final)

