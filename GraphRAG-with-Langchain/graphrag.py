from langchain_core.runnables import  RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_experimental.graph_transformers import LLMGraphTransformer
from neo4j import GraphDatabase
from yfiles_jupyter_graphs import GraphWidget
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(r'C:\upwork_client\compliance_regulatory\GraphRAG-with-Hermes-2.5-Pro-LLM-using-neo4j-database', ".env")

load_dotenv()
load_dotenv(dotenv_path, override=True)

load_dotenv(dotenv_path='.env')

NEO4J_URI="neo4j+s://327bcd80.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="uTWB9vqabe0FGomFYYW_DC3alnAQQeSgGjNtYbhYZaI"
os.environ["NEO4J_URI"] = NEO4J_URI
os.environ["NEO4J_USERNAME"] = NEO4J_USERNAME
os.environ["NEO4J_PASSWORD"] = NEO4J_PASSWORD
graph = Neo4jGraph()

from openai import OpenAI
from utils.tokenizer import OpenAITokenizerWrapper
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
tokenizer = OpenAITokenizerWrapper()  # Load our custom tokenizer for OpenAI
MAX_TOKENS = 2048  # text-embedding-3-small's maximum context length


converter = DocumentConverter()
result = converter.convert(r"C:\upwork_client\compliance_regulatory\rag\Data\bcbs189.pdf")

# --------------------------------------------------------------
# Apply hybrid chunking
# --------------------------------------------------------------

chunker = HybridChunker(
    tokenizer=tokenizer,
    max_tokens=MAX_TOKENS,
    merge_peers=True,
)

chunk_iter = chunker.chunk(dl_doc=result.document)
chunks = list(chunk_iter)

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
llm_transformer = LLMGraphTransformer(llm=llm)
from langchain_core.documents import Document

converted_chunks = [
    Document(
        page_content=chunk.text,
        metadata={"headings": chunk.meta.headings, "page_number": chunk.meta.doc_items[0].prov[0].page_no}
    )
    for chunk in chunks
]

graph_documents = llm_transformer.convert_to_graph_documents(converted_chunks)

graph.add_graph_documents(graph_documents,baseEntityLabel=True,include_source=True)

