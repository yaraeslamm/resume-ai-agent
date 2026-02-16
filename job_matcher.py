from sentence_transformers import SentenceTransformer
import numpy as np
from langchain_community.llms import Ollama
from llm_config import llm


# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# llm = Ollama(model="llama3")

def compute_similarity(resume_text, job_description):
    resume_embedding = embedding_model.encode(resume_text)
    job_embedding = embedding_model.encode(job_description)

    similarity = np.dot(resume_embedding, job_embedding) / (
        np.linalg.norm(resume_embedding) * np.linalg.norm(job_embedding)
    )

    return float(similarity)

def analyze_job_match(resume_text, job_description):

    similarity_score = compute_similarity(resume_text, job_description)

    prompt = f"""
You are an expert career advisor.

Compare the resume and job description below.

Provide:

1. Match Score (0-100 based on alignment)
2. Key Matching Skills
3. Missing or Weak Skills (If none, explicitly say "No critical skills missing.")
4. Concrete Suggestions to Improve Alignment (If none, explicitly say "No significant improvements needed.")

Be honest and do not invent issues just to fill sections.

Resume:
{resume_text}

Job Description:
{job_description}

Note:
The semantic similarity score is {round(similarity_score * 100, 2)}%.
Use it as supporting signal but perform your own reasoning.
"""

    response = llm.invoke(prompt)
    if hasattr(response, "content"):
      return similarity_score, response.content
    return similarity_score, response
