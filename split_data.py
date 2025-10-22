from langchain.text_splitter import RecursiveCharacterTextSplitter
from load_data import all_text

splited_data = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap= 100
)

FIXED_CHUNK_COUNT = 5

for text in all_text:
    chunks = splitter.split_text(text)

    if len(chunks) < FIXED_CHUNK_COUNT:
        chunks += [""] * (FIXED_CHUNK_COUNT - len(chunks))
    else:
        chunks = chunks[:FIXED_CHUNK_COUNT]

    splited_data.append(chunks)

    # splited_data.append(splitter.split_text(i))

# for i in range(len(splited_data)):
#     print(splited_data[i])
#     print("*"*100)