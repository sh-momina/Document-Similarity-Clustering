# from load_data import file_names
# from cosine_similarity import similarity_matrix,similarity_matrix2
# import streamlit as st
# from load_data import all_text

# st.title("Assignment checker")
# st.write("##### Texts below")

# for i in range(len(similarity_matrix2)):
#     for j in range(len(similarity_matrix2)):
#         if i != j:
#             print(f"\n{file_names[i]},{file_names[j]}, -> {similarity_matrix2[i][j]}")


# print("_"*95)
# for i in range(len(similarity_matrix)):
#     for j in range(len(similarity_matrix)):
#         if i != j:
#             print(f"\n{file_names[i]},{file_names[j]}, -> {similarity_matrix[i][j]}")


# def find_clusters():
    
#     for i in range(len(all_text)):
#         st.write(file_names[i])
#         st.write(all_text[i])
#         st.write("____________________________________________________________________________")
    
#     st.write("##### Output below")
#     st.write("\n##### Similarity by using TF-IDF : \n",similarity_matrix)
#     st.write("\n##### Clusters as per TF-IDF : \n")

#     matrix = similarity_matrix

#     threshold = 0.6

#     visited = set()
#     clusters = []

#     for i in range(len(file_names)):
#         if i in visited:
#             continue
#         cluster = [file_names[i]]
#         visited.add(i)

#         for j in range(len(file_names)):
#             if j not in visited and matrix[i][j] >= threshold:
#                 cluster.append(file_names[j])
#                 visited.add(j)

#         clusters.append(cluster)

#     # Print results
#     cluster_number = 1
#     for cluster in clusters:
#         st.write("Cluster", cluster_number, ":", cluster)
#         cluster_number += 1
        
#     st.write("_"*90)
#     st.write("\n##### Similarity by using OpenAI Embeddings : \n",similarity_matrix2)
#     st.write("\n##### Clusters as per OpenAI Embedding : \n")

#     matrix = similarity_matrix

#     threshold = 0.6

#     visited = set()
#     clusters = []

#     for i in range(len(file_names)):
#         if i in visited:
#             continue
#         cluster = [file_names[i]]
#         visited.add(i)

#         for j in range(len(file_names)):
#             if j not in visited and matrix[i][j] >= threshold:
#                 cluster.append(file_names[j])
#                 visited.add(j)

#         clusters.append(cluster)

#     # Print results
#     cluster_number = 1
#     for cluster in clusters:
#         st.write("Cluster", cluster_number, ":", cluster)
#         cluster_number += 1
        
# find_clusters()
from load_data import file_names
from cosine_similarity import similarity_matrix,similarity_matrix2
import streamlit as st
from load_data import all_text

st.title("Assignment checker")
st.write("##### Texts below")

for i in range(len(similarity_matrix2)):
    for j in range(len(similarity_matrix2)):
        if i != j:
            print(f"\n{file_names[i]},{file_names[j]}, -> {similarity_matrix2[i][j]}")


print("_"*95)
for i in range(len(similarity_matrix)):
    for j in range(len(similarity_matrix)):
        if i != j:
            print(f"\n{file_names[i]},{file_names[j]}, -> {similarity_matrix[i][j]}")


def find_clusters():
    
    for i in range(len(all_text)):
        st.write(file_names[i])
        st.write(all_text[i])
        st.write("____________________________________________________________________________")
    
    st.write("##### Output below")
    st.write("\n##### Similarity by using TF-IDF : \n",similarity_matrix)
    st.write("\n##### Clusters as per TF-IDF : \n")

    matrix = similarity_matrix

    threshold = 0.6

    visited = set()
    clusters1 = []

    for i in range(len(file_names)):
        if i in visited:
            continue
        cluster = [file_names[i]]
        visited.add(i)

        for j in range(len(file_names)):
            if j not in visited and matrix[i][j] >= threshold:
                cluster.append(file_names[j])
                visited.add(j)

        clusters1.append(cluster)

    # Print results
    cluster_number = 1
    for cluster in clusters1:
        st.write("Cluster", cluster_number, ":", cluster)
        cluster_number += 1
        
    st.write("_"*90)
    st.write("\n##### Similarity by using OpenAI Embeddings : \n",similarity_matrix2)
    st.write("\n##### Clusters as per OpenAI Embedding : \n")

    matrix = similarity_matrix2

    threshold = 0.6

    visited = set()
    clusters2 = []

    for i in range(len(file_names)):
        if i in visited:
            continue
        cluster = [file_names[i]]
        visited.add(i)

        for j in range(len(file_names)):
            if j not in visited and matrix[i][j] >= threshold:
                cluster.append(file_names[j])
                visited.add(j)

        clusters2.append(cluster)

    # Print results
    cluster_number = 1
    for cluster in clusters2:
        st.write("Cluster", cluster_number, ":", cluster)
        cluster_number += 1
        
find_clusters()
