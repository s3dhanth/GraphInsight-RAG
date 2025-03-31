## Knowledge Graph creation using Pydantic_AI and Groq (Llama 3.3 70b)

This SubParts focuses on designing and implementing the ontology structure to drive the pydatic Framework for structed output.  Using LLMs like Groq's LLaMA-3.3 and OpenAI’s GPT-4o-mini, this system extracts and maps relationships between entities, transforming unstructured text into an insightful, queryable knowledge graph.

## 🏗️ Pipeline Overview

✅ Using Pydantic to validate (force) the schema for Entity Extraction.

## Framework Flow Structure 
![image](https://github.com/user-attachments/assets/88b703f6-e9d6-475d-a5da-1cc6e4449735)

📂 Dataset

We use an ontology-based approach with structured graph relationships. Data sources include:

Primary Dataset: Dev.to Articles - > Contains 

Ontology Definitions (Turtle File): SKOS-based Metadata

Graph Schema: RDF & OWL-based structuring for better entity representation


🛠️ Tech Stack

Graph Database: Neo4j with Cypher Query Language

LLMs: Groq (LLaMA-3.3-70B) & OpenAI GPT-4o-mini

Entity Extraction: Pydantic-AI with structured schema validation

Ontology Frameworks: OWL, RDF, RDFS


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

Fetching entity relationships:
![image](https://github.com/user-attachments/assets/c9b60d34-6120-4469-b36a-976c39b0cb18)



📌 Future Enhancements

🚀 Semantic Search Integration - Use vector embeddings for hybrid search
🔗 Enhanced Ontology Linkage - Improved entity-to-concept mapping

