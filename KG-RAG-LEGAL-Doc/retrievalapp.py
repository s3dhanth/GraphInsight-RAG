import streamlit as st
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
 # Replace with your actual module
from rdflib import Graph

# Load environment variables
dotenv_path = os.path.join(r'C:\upwork_client\compliance_regulatory', ".env")
load_dotenv(dotenv_path, override=True)

# Neo4j connection
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "12345678")
driver = GraphDatabase.driver(URI, auth=AUTH)

# Load ontology and initialize schema
g = Graph()
neo4j_schema3 = getNLOntology(g.parse(r"C:\upwork_client\compliance_regulatory\legaldoc\streamlitonto\charter.ttl"))

# Initialize LLM and retriever
llm = OpenAILLM(model_name="gpt-4o-mini")
examples = [
    "USER INPUT: 'List articles in TITLE 4' QUERY: MATCH (t:Title {titleID: 'TITLE IV'})-[:hasArticle]->(a:Article) RETURN a.articleNumber, a.articleTitle"
]
retriever = Text2CypherRetriever(
    driver=driver,
    llm=llm,  # type: ignore
    neo4j_schema=neo4j_schema3,
    neo4j_database="law",
    examples=examples
)

# Function to call LLM with retrieved context
def get_chat_response(messages, context: str) -> str:
    system_prompt = f"""You are a helpful assistant that answers questions based on the provided context.
Use only the information from the context to answer questions. If you're unsure or the context doesn't contain the relevant information, say so.

Context:
{context}
"""
    messages_with_context = [{"role": "system", "content": system_prompt}, *messages]
    stream = llm.client.chat.completions.create(  # type: ignore
        model="gpt-4o-mini",
        messages=messages_with_context,
        temperature=0.7,
        stream=True,
    )
    return st.write_stream(stream)

# Streamlit UI starts here
st.set_page_config(page_title="LegalDoc Q&A", page_icon="⚖️")
st.title("⚖️ LegalDoc Q&A - Neo4j")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Accept user input
if prompt := st.chat_input("Ask a question related to legal documents"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.status("Generating Cypher query and fetching context..."):
        # Generate query and results
        result = retriever.search(query_text=prompt)
        cypher_query = result.metadata['cypher']
        retrieved_texts = [item.content for item in result.items]
        context = "\n\n".join(retrieved_texts)

        st.markdown("### 🔍 Generated Cypher Query")
        st.code(cypher_query, language="cypher")

        st.markdown("### 📄 Retrieved Context")
        for idx, chunk in enumerate(retrieved_texts):
            st.markdown(f"**Section {idx + 1}**")
            st.markdown(chunk)

    with st.chat_message("assistant"):
        response = get_chat_response(st.session_state.messages, context)
        st.session_state.messages.append({"role": "assistant", "content": response})
