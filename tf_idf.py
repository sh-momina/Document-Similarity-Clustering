
from sklearn.feature_extraction.text import TfidfVectorizer
from load_data import all_text
import numpy as np

vectorize = TfidfVectorizer()

feature_names = []

final_vectors = vectorize.fit_transform(all_text)

means = []
dense_vectors = []

for vec in final_vectors:

        # print("\n",vec,"\n")
        dense = vec.toarray().flatten()
        # print("\n",dense,"\n")

        dense_vectors.append(dense)
        # print("\n",dense.shape,"\n")


    