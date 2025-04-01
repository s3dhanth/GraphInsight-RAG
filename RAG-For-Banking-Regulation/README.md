# RAG-based-LLM-Q-A-Chatbot-App-For-Banking Regulations

This repository contains a Gradio application for an RAG Q&A bot with port 8760 that leverages Groq model (OpenAi can be used also) and Pinecone Vector Database. The app allows users to interact with the Model and get responses based on their queries.

## DataSet
### Banking Regulation Basel Framework
The document outlines key regulatory principles and risk management frameworks for banks and financial institutions.
It discusses capital adequacy requirements, liquidity risk management, and operational risk controls.
There is an emphasis on Basel III framework, which strengthens capital and liquidity standards.

## Selection of Embedings
- Open AI Embdeddings
## Chunking Strategy (Hybrid)
- We have used Contextual Chunking. To set the chunnk size based on contextual Information.
- Serialization of chunks -> (To keep the format intact)(benefits in retrieving Table's).


## Overview of files
### Vector Store.py
- Scan the Document which is in a pdf Format, Splits them into Chunks along with Metadata.
- Populate the chunks into the vector Database To proceed with retrieval.
![image](https://github.com/user-attachments/assets/e0b41842-5bb1-4d9d-aff6-313fe6153df6)


### retrieval.py 
- added functionality of chat history to get more context
- Work Flow user query -> converted to NER (spacy) -> if Person is detected -> Do the metadata filtering with that Author
####Example
### ChatBot Interface (Streamlit) running in port 8760 (History chat support)
### Expected Response (From Basel Document)
![image](https://github.com/user-attachments/assets/e9ccfffb-5e86-4285-8058-9270328fda39)

### Generated Response
![image](https://github.com/user-attachments/assets/3169ad0c-7bc1-46dc-88ce-de9ce3ebedbe)

### Chunks Validation
![image](https://github.com/user-attachments/assets/d6b79127-f0e7-4263-867a-d13b8d964d27)


### Unit Testing using PyTest for (model evaluation)


## Installation

1. Clone the repository:

```sh
git clone https://github.com/s3dhanth/RAG-For-Banking-Regulationgit

cd RAG-Chatbot-utilising-Name-Entity-Recognition
sh
Copy code
pip install -r requirements.txt


run python vectorstore.py

## to run chatbot
streamlit run retrieval.py


# Gradio Application
- Go to port 7860 (local host) for gradio


```

