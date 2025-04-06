# 🔍 Ontology-Aware GraphRAG Pipeline for Regulatory Compliance (Basel Documents)

This repository contains a **Regulatory Compliance Q&A pipeline** that leverages **LLMs**, **Neo4j Knowledge Graph**, and **LangChain** to extract and expand semantic information from financial regulatory documents (e.g., Basel Accords like `bcbs189.pdf`).

---

## ⚙️ Overview

This system performs the following steps:

1. **Entity Extraction** from user queries using a system prompt (LLM-based).
2. **Graph Expansion** using extracted entities via Neo4j Cypher queries.
3. **Knowledge Graph Construction** from regulatory PDFs using chunking + LLM graph transformation.
4. **Streamlined Query Execution Pipeline** via LangChain.

---

## 🛠️ Technologies Used

- `LangChain` (LLMs, prompts, pipelines)
- `Neo4j` (Graph database)
- `LLMGraphTransformer` (LangChain Experimental)
- `HybridChunker` + `OpenAITokenizerWrapper` for document preprocessing
- `Streamlit` (optional frontend)
- `Pydantic` for structured validation
- `OpenAI GPT-4o-mini` (can be swapped with other models)

---

## 🧱 Pipeline Modules

### 📍 Entity Models (`pydantic`)
Defines structured response schema for extracted entities.

```python
class Entity(BaseModel):
    name: str
    type: str  # e.g., "Requirement", "Institution", "Risk Type", etc.
