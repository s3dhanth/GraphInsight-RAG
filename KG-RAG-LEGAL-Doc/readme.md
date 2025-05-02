# 📘 GraphRAG: Legal Document Knowledge Graph Q&A

GraphRAG is an end-to-end pipeline that extracts structured knowledge from unstructured legal documents, stores it in a Neo4j graph database, and enables natural language question answering using Retrieval-Augmented Generation (RAG).

---

## 💡 Features

- Extracts hierarchical structure (Title > Article) from legal documents
- Converts extracted data into structured CSV format
- Defines legal ontology using OWL/RDF
- Imports structured data and ontology into Neo4j using the Data Importer
- Supports two querying strategies:
  - Text-to-Cypher (LLM-generated queries)
  - Static Cypher queries for parent-child relations
- Streamlit interface for user-friendly legal Q&A

---

## Dataset Overview
- The document is the Charter of Fundamental Rights of the European Union (2012). It outlines the fundamental rights and freedoms protected within the EU, structured into seven titles
---
## 🧱 Architecture

1. **HTML Extraction**

   - Fetches HTML from [EU Charter](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT)
   - Parses and structures it into Titles and Articles

2. **CSV Generation**

   - Saves extracted `titles.csv` and `articles.csv` for further use

3. **Ontology Design**

   - Designed in RDF/TTL format (e.g., `charter.ttl`) (protege)
   - Loaded into Neo4j for structured reasoning

4. **Neo4j Graph DB Setup**

   - Uses Neo4j Desktop with Data Importer
   - Maps CSV to ontology schema
![image](https://github.com/user-attachments/assets/7b27b9db-426d-4454-90aa-bb136153ba98)

   

5. **Cypher Query Generation**

   - `Text2CypherRetriever` with OpenAI's GPT-4o-mini generates Cypher queries from user prompts
   - Alternatively, predefined static Cypher queries are used

6. **Frontend with Streamlit**

   - Conversational chatbot interface
   - Accepts natural language questions
   - Displays generated Cypher, retrieved content, and AI response

---

## 📁 Folder Structure

```

├── legaldoc/
│   ├── streamlitonto/
│   │   └── charter.ttl            # Ontology
│   └── titles.csv                 # Title hierarchy
│   └── articles.csv               # Extracted legal content
├── app.py                         # Streamlit UI
├── text2cypher.py                 # Text-to-Cypher retriever logic
├── utils.py                       # HTML parsing and CSV generation
└── .env                           # Environment variables
```

---

## 🚀 Run the Project

### 1. Install Dependencies

```bash
pip install streamlit neo4j pandas beautifulsoup4 openai
```

### 2. Set up Neo4j

- Use the Data Importer to load `titles.csv` and `articles.csv`
- Apply the ontology (`charter.ttl`) as schema
![image](https://github.com/user-attachments/assets/69f98cf9-590e-47d1-937c-1d7ad52d34af)

### 3. Add your environment variables in `.env`

```env
OPENAI_API_KEY=your_openai_key
```

### 4. Launch the Streamlit App

```bash
streamlit run retrievalapp.py
```

---

## 🧠 Example Queries

- ### "List articles in TITLE IV"
![image](https://github.com/user-attachments/assets/7bbfa304-dab2-47b7-976a-2ecd4882f886)

- ### "articleTitle - Protection of personal data , belongs to which title?"
![image](https://github.com/user-attachments/assets/9a9e2956-718a-4eae-a26f-fa96e48568d9)

The app will:

- Generate the appropriate Cypher query
- Fetch relevant nodes and relationships from Neo4j
- Use OpenAI LLM to generate responses based on retrieved data

---

## 🛠️ Future Work

- Improve ontology alignment for deeper legal reasoning
- Expand dataset to include multiple legal documents
- Add visualization using Graph Data Science

---

## 📜 License

MIT License

---

---

## 🚀 Phase 2: Introducing Graph Enrichment & Hybrid Retrieval

This phase extends the pipeline with:

- LLM-driven entity extraction
- Graph-based symbolic retrieval via Neo4j Fulltext indexes
- Vector-based semantic search using OpenAI embeddings
- Hybrid retrieval combining graph and vector contexts
- Natural language response generation via GPT-4o

---
# 🧠 Phase 2 Features

### ✅ Hybrid Legal Knowledge Retrieval

#### Entity-Aware Graph Scoring

- Extracts entities like `laws`, `actions`, `organizations` using LLM
- Searches Neo4j `entity_up` fulltext index
- Traverses `MENTIONS` relationships from matched nodes
- Builds graph view for RAG prompt

#### Semantic Vector Search

- Embeds text using OpenAI embeddings
- Stores in Neo4j vector index
- Retrieves top-k semantically similar chunks to the query

#### Unified RAG Chain

Both graph and vector retrieval are combined in the final prompt:

https://github.com/user-attachments/assets/8ad18417-f84a-4985-8e6b-0227418d10e5


