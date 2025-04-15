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

## 🧱 Architecture

1. **HTML Extraction**

   - Fetches HTML from [EU Charter](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT)
   - Parses and structures it into Titles and Articles

2. **CSV Generation**

   - Saves extracted `titles.csv` and `articles.csv` for further use

3. **Ontology Design**

   - Designed in RDF/TTL format (e.g., `charter.ttl`)
   - Loaded into Neo4j for structured reasoning

4. **Neo4j Graph DB Setup**

   - Uses Neo4j Desktop with Data Importer
   - Maps CSV to ontology schema

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
compliance_regulatory/
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

- Launch Neo4j Desktop or Docker container
- Use the Data Importer to load `titles.csv` and `articles.csv`
- Apply the ontology (`charter.ttl`) as schema

### 3. Add your environment variables in `.env`

```env
OPENAI_API_KEY=your_openai_key
```

### 4. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🧠 Example Queries

- "List articles in TITLE IV"
- "What is Article 7 about?"
- "Summarize TITLE III"

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

## 🤝 Acknowledgements

- [Neo4j](https://neo4j.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [EU Legal Charter](https://eur-lex.europa.eu/)


