from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
import pandas as pd
from sentence_transformers import SentenceTransformer
import spacy
from fuzzywuzzy import fuzz, process
from pinecone import Pinecone
import spacy
from query_rag_spector import retrieve_from_pinecone
from query_rag_spector import retrive_from_chatbot

nlp = spacy.load("en_core_web_lg")
stored_meta = pd.read_csv('arxiv_metadata.csv')
model = SentenceTransformer('allenai-specter')
api_key = 'd7204d21-cb62-4544-b49c-9169b420c0e1'

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""



def test_conclusion_and_future_workr():
    assert query_and_validate(
        question = "what are the components of capital?",
        expected_response = "Total regulatory capital will consist of the sum of the following elements: 1. Tier 1 Capital (going-concern capital) a. Common Equity Tier 1 b. Additional Tier 1 2. Tier 2 Capital (gone-concern capital)")

def test_conclusion_and_future_workr1():
    assert query_and_validate(
        question = "Explain liquidity Coverage Ratio.?"
",
        expected_response = "The LCR is intended to promote resilience to potential liquidity disruptions over a thirty day horizon. It will help ensure that global banks have sufficient unencumbered, highquality liquid assets to offset the net cash outflows it could encounter under an acute shortterm stress scenario. The specified scenario is built upon circumstances experienced in the global financial crisis that began in 2007 and entails both institution-specific and systemic shocks.")

def test_conclusion_and_future_workr2():
    assert query_and_validate(
        question = "How does BCBS 189 address operational risk?",
        expected_response = "It suggests implementing robust internal controls, risk assessment procedures, and contingency plans to mitigate operational failures.")

def test_conclusion_and_future_workr4():
    assert query_and_validate(
        question = "What is the importance of stress testing according to BCBS 189?",
        expected_response = "Stress testing helps institutions identify potential vulnerabilities by simulating extreme financial scenarios.")
    
def test_conclusion_and_future_workr5():
    assert query_and_validate(
        question = "How does BCBS 189 recommend banks handle high-risk exposures?",
        expected_response = "Banks should regularly assess risk exposures, set concentration limits, and diversify their asset portfolios to mitigate risks.")


def query_and_validate(question: str, expected_response: str):
    
    results = retrieve_from_pinecone(question)
    response_text =retrive_from_chatbot(question,results)
        
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = Ollama(model="llama3.1")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )
