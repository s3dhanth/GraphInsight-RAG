
import os
from typing import List
from pydantic import BaseModel, Field
from neo4j import GraphDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain.chat_models import ChatOpenAI

# --- 1. Entity Model Definitions ---
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
class Entity(BaseModel):
    name: str = Field(..., description="The name of the extracted entity.")
    type: str = Field(
        ..., 
        description="The type/category of the entity. Examples: 'Requirement', 'Authority', 'Risk Type', 'Institution', 'Disclosure', 'Timeframe', 'Threshold', 'Principle'."
    )

class EntityExtraction(BaseModel):
    entities: List[Entity]


# --- 2. Entity Extraction Prompt ---

entity_prompt = ChatPromptTemplate.from_template("""
You are a regulatory compliance assistant specialized in Basel documentation (e.g., bcbs189.pdf).

From the user query below, extract all relevant regulatory **entities** and assign an appropriate **type** to each. 

Use the following types **when applicable**, but feel free to use other custom types if something doesn't fit well:
- "Requirement"
- "Authority"
- "Risk Type"
- "Institution"
- "Disclosure"
- "Timeframe"
- "Threshold"
- "Principle"

The goal is to **not miss any important concept**. For each entity, choose a type that best describes it, even if it's not in the list above.

Return the response in **JSON** format as shown below:

{{
  "entities": [
    {{
      "name": "Entity Name", 
      "type": "Entity Type"
    }}
  ]
}}

User Query: "{query}"
""")

# --- 3. Cypher Query Function Using :MENTIONS ---

def run_custom_cypher(entity_name: str) -> str:
    uri = os.environ["NEO4J_URI"]
    user = os.environ["NEO4J_USERNAME"]
    pwd = os.environ["NEO4J_PASSWORD"]
    driver = GraphDatabase.driver(uri, auth=(user, pwd))

    cypher = """
    CALL db.index.fulltext.queryNodes('entity_id_index', $query, {limit: 2})
    YIELD node, score
    CALL {
  WITH node
  MATCH (node)-[r]->(neighbor)
  RETURN properties(node) AS source_properties, type(r) AS relation, properties(neighbor) AS target_properties
  UNION ALL
  WITH node
  MATCH (node)<-[r]-(neighbor)
  RETURN properties(neighbor) AS source_properties, type(r) AS relation, properties(node) AS target_properties
}
RETURN source_properties, relation, target_properties

    """
    with driver.session() as session:
        result = session.run(cypher, {"query": entity_name})
        outputs = []
        for record in result:
            source_props = record.get("source_properties", {})
            target_props = record.get("target_properties", {})
            relation = record.get("relation", "MENTIONS")
            outputs.append(
        f"{source_props.get('id', 'Unknown')} [{source_props.get('headings', 'no-heading')}] "
        f"-[:{relation}]-> "
        f"{target_props.get('id', 'Unknown')} [{target_props.get('headings', 'no-heading')}]"
    )
        
    driver.close()
    return "\n".join(outputs)


# --- 4. LangChain Pipeline ---

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")  # or gpt-3.5-turbo

# Extract entities from query
extract_entities_chain = entity_prompt | llm | RunnableLambda(lambda x: EntityExtraction.parse_raw(x.content).entities)

# Expand graph context for each entity using Neo4j
def query_neo4j_for_all_entities(entities: List[Entity]) -> str:
    all_outputs = []
    for entity in entities:
        context = run_custom_cypher(entity.name)
        all_outputs.append(f"### {entity.name} ({entity.type})\n{context}")
    
    return "\n\n".join(all_outputs)

neo4j_context_chain = RunnableLambda(query_neo4j_for_all_entities)

# Combined pipeline
full_pipeline = RunnablePassthrough() | extract_entities_chain | neo4j_context_chain


if __name__ == "__main__":
    query = "What is the primary objective of the principles outlined in this document?"
    result = full_pipeline.invoke(query)
    print("=== Expanded KG Context ===\n")
    print(result)

