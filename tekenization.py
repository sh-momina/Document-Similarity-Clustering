import spacy
from load_data import all_text

tokenize_data = []

nlp = spacy.load("en_core_web_sm")

for i in all_text:
    list = []
    data = nlp(i)
    for j in data:
        if not j.is_stop or not j.is_punct:
            list.append(j.lower_)
    tokenize_data.append(list)
    
# print(tokenize_data) 