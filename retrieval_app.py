import gradio as gr
from neo4j import GraphDatabase
from neo4j_graphrag.retrievers import Text2CypherRetriever
from neo4j_graphrag.llm.openai_llm import OpenAILLM
from utils import getNLOntology
from rdflib import Graph
import nest_asyncio
from dotenv import load_dotenv
import os

# Enable nested event loops for async operations
nest_asyncio.apply()

# Load environment variables
dotenv_path = os.path.join(r'C:\upwork_client\compliance_regulatory', ".env")
load_dotenv(dotenv_path, override=True)

# Neo4j connection details
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "12345678")
driver = GraphDatabase.driver(URI, auth=AUTH)

# Initialize OpenAI LLM
llm = OpenAILLM(model_name="gpt-4o-mini")

# Load the ontology
g = Graph()
ontology_path = r"C:\upwork_client\compliance_regulatory\session 31\onto\Bankingontology2.ttl"
neo4j_schema = getNLOntology(g.parse(ontology_path))

# Define example queries
examples = ["Which regulations apply to IBM?"]

# Initialize the retriever
retriever = Text2CypherRetriever(
    driver=driver,
    llm=llm,
    neo4j_schema=neo4j_schema,
    neo4j_database="banking5",
    examples=examples
)

# Function to process user input and return Neo4j results
def query_neo4j(user_input):
    result = retriever.search(query_text=user_input)
    cypher_query = result.metadata['cypher']
    
    # Extract response content
    response_data = [item.content for item in result.items]

    return f"**Generated Cypher Query:**\n```\n{cypher_query}\n```\n\n**Response:**\n{response_data}"

# Gradio Interface
iface = gr.Interface(
    fn=query_neo4j,
    inputs=gr.Textbox(label="Enter your question"),
    outputs=gr.Markdown(),
    title="💡 Basel II Regulatory Chatbot",
    description="Ask any question related to Basel II regulations. The chatbot will generate a Cypher query and fetch the relevant results from Neo4j."
)

# Launch the application
iface.launch()