import os
from langchain.llms import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.getcwd(), ".env")

load_dotenv(dotenv_path, override=True)

# it's the legal document
uri = "bolt://localhost:7687"  # Adjust if your database is hosted elsewhere
username = "neo4j"
password = "12345678"
question = "what is an unavailable deposit and how does it become unavailable?"

Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(),
    url=uri,
    username=username,
    password=password,
    index_name='combined_index',
    node_label="Embeddable",
    text_node_properties=["textForEmbedding"],
    embedding_node_property='combinedEmbedding'
)
