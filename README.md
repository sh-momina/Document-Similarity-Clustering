# 🧩 Document Similarity Clustering

A Streamlit app that clusters assignment documents (`.docx`) using both **TF-IDF** and **OpenAI embeddings** via **LangChain**.  
It helps detect similar or duplicate assignments by comparing semantic and keyword-level similarities.

---

## 🚀 Features
- 📤 Upload multiple `.docx` or `.pdf` files  
- 🧠 Dual analysis using **TF-IDF** and **OpenAI embeddings**  
- 🔍 Clusters similar assignments based on content meaning  
- 💬 Displays similarity scores, strengths, and recommendations  
- 🌐 Simple **Streamlit UI** for interactive results  

---

## 🧠 Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI Embeddings**
- **TF-IDF (scikit-learn)**
- **Unstructured** (for text extraction)

---

## ⚙️ Run Locally
```bash
git clone https://github.com/sh-momina/Document-Similarity-Clustering.git
cd Document-Similarity-Clustering
streamlit run clusters.py
