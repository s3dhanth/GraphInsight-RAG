import asyncio, os
from neo4j import GraphDatabase
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.experimental.components.text_splitters.fixed_size_splitter import FixedSizeSplitter
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline
from neo4j_graphrag.llm.openai_llm import OpenAILLM
from neo4j_graphrag.experimental.components.resolver import SinglePropertyExactMatchResolver
from rdflib import Graph
from utils import getSchemaFromOnto, getPKs
from rdflib_neo4j import Neo4jStore, Neo4jStoreConfig, HANDLE_VOCAB_URI_STRATEGY
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "your_password"
import nest_asyncio
from dotenv import load_dotenv
import os
import json

nest_asyncio.apply()
dotenv_path = os.path.join(r'C:\upwork_client\compliance_regulatory', ".env")

load_dotenv(dotenv_path, override=True)
# Connect to the Neo4j database
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
embedder = OpenAIEmbeddings(model = 'text-embedding-3-small')
g = Graph()

#neo4j_schema2 = getSchemaFromOnto(g.parse(r"C:\Users\ashut\Pictures\newonto.ttl"))
# Create a Splitter object
neo4j_schema = getSchemaFromOnto(g.parse(r"C:\compliance_regulatory\session 31\onto\Bankingontology2.ttl"))
splitter = FixedSizeSplitter(chunk_size=2500, chunk_overlap=10)

llm = OpenAILLM(
    model_name="gpt-4o-mini",
    model_params={
        "max_tokens": 5000,
        "response_format": {"type": "json_object"},
        "temperature": 0,
    },
)
auth_data = {'uri': 'neo4j://localhost:7687',
             'database': 'your_db',
             'user': NEO4J_USERNAME,
             'pwd': NEO4J_PASSWORD,}

kg_builder = SimpleKGPipeline(
    llm=llm,
    driver=driver,
    text_splitter=splitter,
    embedder=embedder,
    entities=list(neo4j_schema.entities.values()),
    relations=list(neo4j_schema.relations.values()),
    potential_schema=neo4j_schema.potential_schema,
    on_error="IGNORE",
    from_pdf=False,
    neo4j_database='your_db',
    perform_entity_resolution=False
)

directory_path = r"C:\upwork_client\compliance_regulatory\session 31\data\redp5748.pdf"


import pdfplumber
def extract_text_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Avoid adding None values
                text += page_text + "\n"
    return text.strip()
# Extract and merge text
merged_text = extract_text_pdfplumber(directory_path)

# Print the extracted text
print(merged_text)
asyncio.run(kg_builder.run_async(text=merged_text))


for pk in getPKs(g):
    resolver = SinglePropertyExactMatchResolver(driver=driver, resolve_property=pk)
    asyncio.run(resolver.run())
for pk in getPKs(g):
    print(f"Running resolver for: {pk}")
    resolver = SinglePropertyExactMatchResolver(driver=driver, resolve_property=pk)
    asyncio.run(resolver.run())
    print(f"Finished resolving for: {pk}")








###  Debugging
a = getPKs(g)
