# 🚀 RAG Chat Assistant with Streamlit

A high-precision Retrieval-Augmented Generation (RAG) system built with **Streamlit**, **FAISS**, and **Hugging Face** models. This assistant allows users to upload a PDF, index its content, and engage in a context-aware conversation using advanced retrieval and reranking techniques.

## 🌟 Key Features

*   **Intelligent Query Rewriting:** Uses `google/flan-t5-large` to transform conversational follow-up questions into standalone search queries.
*   **High-Precision Retrieval:** Employs `BAAI/bge-base-en-v1.5` for state-of-the-art semantic search.
*   **Two-Stage Search:** Implements a Reranking stage using `BAAI/bge-reranker-base` to ensure the most relevant context is provided to the LLM.
*   **Metadata Filtering:** Allows users to narrow down searches to specific pages of the document.
*   **Conversational Memory:** Maintains a history of the chat for seamless multi-turn interactions.
*   **Debug Mode:** Includes an expander to view rewritten queries and retrieved source chunks.

## 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss)
*   **Models:**
    *   **Embeddings:** `BAAI/bge-base-en-v1.5`
    *   **Reranker:** `BAAI/bge-reranker-base`
    *   **LLM (Generation):** `google/flan-t5-large`
*   **PDF Processing:** `pypdf`
*   **Framework:** `sentence-transformers`, `transformers`, `torch`

## 📋 Prerequisites

*   Python 3.8+
*   Git

## ⚙️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Shivam1026/RAG-app-with-Streamlit.git
    cd RAG-app-with-Streamlit
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### 1. Process your PDF
Place your PDF file (e.g., `Articles.pdf`) in the project root and run the ingestion script to create the FAISS index and metadata:
```bash
python process_pdf.py
```

### 2. Launch the App
Start the Streamlit interface:
```bash
streamlit run app.py
```

## 📂 Project Structure

*   `app.py`: The main Streamlit application logic and UI.
*   `process_pdf.py`: Script to extract text from PDF, chunk it, and build the FAISS vector index.
*   `requirements.txt`: List of required Python packages.
*   `index.faiss`: The generated vector database (built during ingestion).
*   `metadata.pkl`: Stores text chunks and associated metadata (built during ingestion).
*   `.gitignore`: Prevents large/unnecessary files (like `venv`) from being uploaded to GitHub.

## 🧠 How it Works (The RAG Pipeline)

1.  **Query Rewriting:** The user's question is rephrased by an LLM to incorporate context from previous messages.
2.  **Initial Retrieval:** The system searches the FAISS index for the top 20 most similar chunks.
3.  **Reranking:** A Cross-Encoder model scores these chunks against the query to find the top 3 most relevant passages.
4.  **Generation:** The top chunks and chat history are sent to `flan-t5-large` to generate a grounded, accurate response.

---
Created by [Shivam1026](https://github.com/Shivam1026)
