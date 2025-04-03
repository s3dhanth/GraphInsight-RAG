# Ontology Driver Graph RAG For Banking Regulations

This repository contains a Streamlit application for an GraphRAG Q&A bot with port 8760 that leverages Groq model (OpenAi can be used also) and neo4j Graph Database. The app allows users to interact with the Model and get responses based on their queries.

## DataSet
### Banking Regulation Basel Framework
The document outlines key regulatory principles and risk management frameworks for banks and financial institutions.
It discusses capital adequacy requirements, liquidity risk management, and operational risk controls.
There is an emphasis on Basel III framework, which strengthens capital and liquidity standards.

## Ontology Design (Integration with FIBO)
- Software Used - Protégé
- Rdfs (From Fibo Git Repository) - contains classes for entities, used for inheritance and comment To ensure integration for Regulation Document
- Ontology Structure Overview.
#### High level overview
- Regulations apply to Financial Entities.
- Risk types require Compliance Measures.
- Regulatory Bodies assess Financial Entities.
![image](https://github.com/user-attachments/assets/5eb63a10-0ba2-41d5-aecd-5c25b8f78f30)
![image](https://github.com/user-attachments/assets/dd6607fc-cfe1-4e6a-99a3-ef4372f142f4)

- Data properties (like names, jurisdictions, and descriptions) provide additional details.
- example
![image](https://github.com/user-attachments/assets/516a3e10-0752-4c2e-bba3-ce855fb0d77c)

## Flowchart Of Entire Graph Rag Pipeline
### Knowledge Graph Construction
![image](https://github.com/user-attachments/assets/5b18798c-ecfe-4ed8-a224-38ebbd31f0b4)
### Retrieval Process
![image](https://github.com/user-attachments/assets/4145c919-d275-4951-ad0e-ebb74066c85b)

## Some examples -
- User Query -> "Which regulations apply to IBM"
- Response (Text2Cypher)
![image](https://github.com/user-attachments/assets/712a4974-a70b-406a-a680-2f49aaebd23b)
#### Neo4j Interface
![image](https://github.com/user-attachments/assets/a8fb34c4-f3d2-408b-8236-3217c543df78)

## Streamlit Interface
![image](https://github.com/user-attachments/assets/8539a300-cbe8-4939-998c-63f44084ff0f)





