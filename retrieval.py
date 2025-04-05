from neo4j import GraphDatabase
from neo4j_graphrag.retrievers import Text2CypherRetriever
from neo4j_graphrag.llm.openai_llm import OpenAILLM
from utils import getNLOntology
from rdflib import Graph
from utils import getNLOntology
import nest_asyncio
from dotenv import load_dotenv
import os
import json

nest_asyncio.apply()
dotenv_path = os.path.join(r'C:\upwork_client\compliance_regulatory', ".env")

load_dotenv(dotenv_path, override=True)
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "your_password")

# Connect to Neo4j database
driver = GraphDatabase.driver(URI, auth=AUTH)

# Create LLM object
llm = OpenAILLM(model_name="gpt-4o-mini")
g = Graph()
neo4j_schema3 = getNLOntology(g.parse(r"C:\upwork_client\compliance_regulatory\session 31\onto\Bankingontology2.ttl"))

#print(neo4j_schema)

# Initialize the retriever
retriever = Text2CypherRetriever(
    driver=driver,
    llm=llm,  # type: ignore
    neo4j_schema=neo4j_schema3,
    neo4j_database="yourdb"
    
)
# Generate a Cypher query using the LLM, send it to the Neo4j database, and return the results
query_text = "Which regulations apply to IBM"
result = retriever.search(query_text=query_text)
print("generated query: \n", result.metadata['cypher'])
for item in result.items:
    print("answer:", item.content)
