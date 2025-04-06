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
- `Pydantic` for structured validation
- `OpenAI GPT-4o-mini` (can be swapped with other models)

---
## KG Construction
![image](https://github.com/user-attachments/assets/87178981-9a6c-46ad-a6a2-89dae2945ca7)

## 🧱 Pipeline Modules
Step 1: Load and Chunk Document
Convert PDF to structured text.

Use a hybrid chunking strategy with heading-awareness and OpenAI tokenizer.

🔹 Step 2: Convert Chunks to Graph Documents
Use LLMGraphTransformer to extract entity-relation triples from each chunk.

Store results in Neo4j, preserving page numbers and heading metadata.

🔹 Step 3: Entity Extraction from Query
A LangChain pipeline with ChatOpenAI extracts entities and types from a user query.

🔹 Step 4: Neo4j Context Retrieval
A custom Cypher query fetches relationships around extracted entities for knowledge expansion.

### 📍 Entity Models (`pydantic`)
Defines structured response schema for extracted entities.


