GraphRAG with Neo4j - Ontology-Powered Knowledge Graph for Advanced Retrieval 🚀

This repository showcases a Graph-based Retrieval-Augmented Generation (RAG) pipeline leveraging Neo4j, OWL ontologies, and RDFS to structure and enhance knowledge retrieval. Using LLMs like Groq's LLaMA-3.3 and OpenAI’s GPT-4o-mini, this system extracts and maps relationships between entities, transforming unstructured text into an insightful, queryable knowledge graph.

📌 Key Features

✅ Ontology-Driven Knowledge Graph - Structured entity relationships with Neo4j & RDFS
✅ Automated Entity Extraction - AI-powered entity linking via Groq & OpenAI
✅ Seamless Query Execution - Cypher-powered graph exploration
✅ Scalable Architecture - Dockerized deployment for efficiency
✅ RAG-based Contextual Retrieval - Enhancing responses with linked knowledge

📂 Dataset

We use an ontology-based approach with structured graph relationships. Data sources include:

Primary Dataset: Dev.to Articles

Ontology Definitions (Turtle File): SKOS-based Metadata

Graph Schema: RDF & OWL-based structuring for better entity representation

🏗️ Pipeline Overview

The flowchart below outlines how data flows from raw text to an enriched knowledge graph for enhanced retrieval:

1️⃣ Data Ingestion - Articles are fetched and preprocessed
2️⃣ Entity Extraction - Named Entity Recognition (NER) with Groq & OpenAI
3️⃣ Graph Construction - Neo4j nodes & relationships mapped via Cypher
4️⃣ Ontology Mapping - Concepts linked using OWL & RDFS schemas
5️⃣ Query Execution - Cypher queries extract relevant data for retrieval
6️⃣ Enhanced RAG Pipeline - Graph-enriched responses generated for user queries

📌 Check the Flowchart Image (Attach Image here)

🛠️ Tech Stack

Graph Database: Neo4j with Cypher Query Language

LLMs: Groq (LLaMA-3.3-70B) & OpenAI GPT-4o-mini

Entity Extraction: Pydantic-AI with structured schema validation

Ontology Frameworks: OWL, RDF, RDFS

Containerization: Docker for Neo4j setup

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/graphRAG.git
cd graphRAG

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Environment Variables

Create a .env file and add:

NEO4J_URL=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=yourpassword

4️⃣ Start Neo4j with Docker

docker-compose up --build

🚀 Running the Pipeline

Once the environment is ready, execute the main pipeline:

python main.py

This will:

Ingest data

Extract entities

Create & map nodes in Neo4j

Enable structured retrieval for queries

🎯 Querying the Knowledge Graph

Sample Cypher query to retrieve article bodies:

MATCH (n:Article) RETURN n.body LIMIT 5;

Fetching entity relationships:

MATCH (e:Entity)-[:refers_to]->(c:Concept) RETURN e, c;

📌 Future Enhancements

🚀 Semantic Search Integration - Use vector embeddings for hybrid search
🔗 Enhanced Ontology Linkage - Improved entity-to-concept mapping
📈 Dashboard for Graph Visualization - Interactive UI with Neo4j Bloom


