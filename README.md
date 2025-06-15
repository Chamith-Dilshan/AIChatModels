# ChatModels Project

A collection of practical AI-powered Python tools and demos, including:
- **Grocery Item Categorizer** (using LLMs)
- **PDF RAG System** (retrieve answers from PDF docs using embeddings and vector DB)
- **Ollama Model Interactions** (via Python library and REST API)
- **Custom Model File Creation** (for local LLMs)

---

## Table of Contents

- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Features](#features)
  - [1. Grocery Item Categorizer](#1-grocery-item-categorizer)
  - [2. PDF RAG System](#2-pdf-rag-system)
  - [3. Using Ollama Python Library](#3-using-ollama-python-library)
  - [4. Using Ollama REST API](#4-using-ollama-rest-api)
  - [5. Custom Model File Creation](#5-custom-model-file-creation)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Project Structure

```
ChatModels/
│
├── groceryApp/
│   ├── categorizer.py
│   └── data/
│       ├── grocery_list.txt
│       └── categorized_grocery_list.txt
│
├── ragSystem/
│   ├── pdf-rag.py
│   └── data/
│       └── python_3.13_doc/
│           └── whatsnew.pdf
│
├── usingOllamaLib.py
├── usingRESTApi.py
└── ...
```

---

## Environment Setup

### 1. Python & Virtual Environment

- Install [Python 3.10+](https://www.python.org/downloads/)
- Create and activate a virtual environment:
  ```sh
  python -m venv myenv
  myenv\Scripts\activate  # On Windows
  ```

### 2. Install Dependencies

- Install required packages:
  ```sh
  pip install -r requirements.txt
  ```
  *(If `requirements.txt` is missing, see each feature section for dependencies.)*

### 3. Install Ollama

- Download and install [Ollama](https://ollama.com/download) for your OS.
- Start the Ollama server:
  ```sh
  ollama serve
  ```

### 4. (Optional) Install Poppler & Tesseract for PDF features

- **Poppler**: [Download for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
  - Extract and add `poppler/bin` to your PATH.
- **Tesseract**: [Download for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
  - Install and add to your PATH.

---

## Features

### 1. Grocery Item Categorizer

Categorizes and sorts grocery items using an LLM.

**How to use:**
1. Edit `groceryApp/data/grocery_list.txt` with your grocery items (one per line).
2. Run:
   ```sh
   python groceryApp/categorizer.py
   ```
3. The categorized list will be saved to `groceryApp/data/categorized_grocery_list.txt`.

**Dependencies:**
- `ollama` Python package

**Model:**
- Uses the `llama3.2` model (ensure it's available in your Ollama instance).

---

### 2. PDF RAG System

Retrieves answers from a PDF using embeddings and a vector database.

**How to use:**
1. Place your PDF in `ragSystem/data/`.
2. Set the `doc_path` in `ragSystem/pdf-rag.py` to your PDF file.
3. Run:
   ```sh
   python ragSystem/pdf-rag.py
   ```
4. Ask questions as prompted.

**Dependencies:**
- `langchain`
- `langchain_community`
- `langchain_ollama`
- `langchain_text_splitters`
- `ollama`
- `chromadb`
- `unstructured`
- `pdf2image`
- `poppler` (system dependency)
- `tesseract` (system dependency, for OCR PDFs)

**Models:**
- Embedding: `nomic-embed-text`
- LLM: `llama3.2`

**Setup Notes:**
- Make sure Poppler and Tesseract are installed and in your PATH for PDF processing.

---

### 3. Using Ollama Python Library

Interact with Ollama models directly from Python.

**How to use:**
- See [`usingOllamaLib.py`](usingOllamaLib.py) for examples.
- Run:
  ```sh
  python usingOllamaLib.py
  ```

**Dependencies:**
- `ollama` Python package

---

### 4. Using Ollama REST API

Interact with Ollama models via HTTP requests.

**How to use:**
- See [`usingRESTApi.py`](usingRESTApi.py) for examples.
- Run:
  ```sh
  python usingRESTApi.py
  ```

**Dependencies:**
- `requests`

---

### 5. Custom Model File Creation

You can create and use your own custom model files with Ollama.  
Refer to [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md) for details.

---

## Troubleshooting

- **Poppler/Tesseract errors:**  
  Ensure both are installed and their `bin` directories are in your system PATH.
- **Ollama errors:**  
  Make sure the Ollama server is running and the required models are pulled.
- **Missing dependencies:**  
  Install missing packages with `pip install <package>`.

---

## License

This project is for educational and demonstration purposes. 
