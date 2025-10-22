from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv
from pdf2image import convert_from_path
from langchain_community.document_loaders import UnstructuredFileLoader
import os

loader = DirectoryLoader(
    path=r"D:\study\projects\LangChain\Assignment_matcher\data",
    glob="**/*",
    loader_cls=UnstructuredFileLoader,
    show_progress=True,
    use_multithreading=True
)

docs = loader.load()

all_text = []
text_metadata = []
file_names = []

for doc in docs:
    file_names.append(os.path.basename(doc.metadata['source']))
    all_text.append(doc.page_content)
    text_metadata.append(doc.metadata)



# for i in range(len(all_text)):
#     print(file_names[i])
#     print(all_text[i])
#     print("*"*100)


























# url = r"D:\study\semester 6\Artifitial intellegence\assignments\Assignment 1\Assignment  1.docx"

# url = r"D:\Chrome downloads\AI_Assignment_1.pdf"

# def get_content(url):

#     file_path = Path(url)
#     extention = file_path.suffix

#     word_docs = []
#     text_docs = []

#     if extention.lower() == ".pdf":
#         loader = PyPDFLoader(url)
#         text_docs = loader.load()

#     elif extention.lower() == ".docx":
#         loader = UnstructuredWordDocumentLoader(url)
#         word_docs = loader.load()
        

#     complete_text = ""

#     a = []
#     if text_docs:
#         a = text_docs
#     if word_docs:
#         a = word_docs

#     for i in range(len(a)):
#         complete_text += f"\npage {i} text data ->" +  a[i].page_content
        
#     return complete_text














# a = text_docs
# if len(text_docs) < len(img_docs):
#     a = img_docs

# for i in range(len(a)):
#     if text_docs[i]:
#         complete_text += f"\npage {i} text data ->" +  text_docs[i].page_content
        
    # if img_docs[i]:
    #     complete_text += f"\npage {i} image data ->" + pytesseract.image_to_string(img_docs[i])
        
# print(complete_text)

# img_docs = convert_from_path(url)

# text = pytesseract.image_to_string(img_docs[5])

# print(text)