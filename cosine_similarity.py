from tf_idf import dense_vectors
from sklearn.metrics.pairwise import cosine_similarity
from openai_embedding import vector_final

similarity_matrix = cosine_similarity(dense_vectors)

similarity_matrix2 = cosine_similarity(vector_final)

# print("Cosine Similarity Matrix:\n")
# print("\nSimilarity by using TF-IDF : \n",similarity_matrix)
# print("\nSimilarity by using OpenAI Embeddings : \n",similarity_matrix2)
