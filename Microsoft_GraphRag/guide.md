# 🔍 Microsoft Graph RAG with Groq + OpenAI Embeddings

This repo demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using [graphrag](https://pypi.org/project/graphrag/) with **Groq's ultra-fast LLMs** and **OpenAI's embedding models**. It processes text files, builds a knowledge graph, and allows both local and global semantic querying.

---

## ⚙️ Tech Stack

- 🧠 **Groq** for LLM inference (`mixtral-8x7b-32768`)
- 🧬 **OpenAI** for embeddings (`text-embedding-3-small`)
- 🕸️ **graphrag** for graph-based RAG
- 🐍 Python 3.11 (via Conda)
- 🔐 Environment variables for secure key management

---

## 🚀 Setup Instructions

### 1. Create & Activate Environment

```bash
conda create -n graphgroq python=3.11 -y
conda activate graphgroq
2. Set Your API Keys

export OPENAI_API_KEY="your-openai-key"
export GROQ_API_KEY="your-groq-key"
3. Install Required Package

pip install graphrag
### 📁 Folder Structure

graph-rag/
├── ragtest/
│   ├── input/
│   │   └── fahd.txt
│   ├── cache/
│   ├── output/
│   └── (auto-generated artifacts)
2. Set Environment Variables

export OPENAI_API_KEY="your-openai-key"
export GROQ_API_KEY="your-groq-key"
3. Install graphrag

pip install graphrag

mkdir -p ./ragtest/input

python3 -m graphrag.index --init --root ./ragtest
python3 -m graphrag.index --root ./ragtest
### 6. Query
python3 -m graphrag.query --root ./ragtest --method global "Give me indepth information about IBM Synthetic Dataset for Payment Cards?"


