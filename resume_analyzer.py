from langchain_community.llms import Ollama
from llm_config import llm

# llm = Ollama(model="llama3")

def analyze_resume(resume_text):
    prompt = f"""
You are an expert ATS resume evaluator.

Analyze the resume below and provide:

1. Overall Score (out of 100)
2. Strengths
3. Weaknesses (If none, explicitly say "No major weaknesses found.")
4. Missing Skills (If none, explicitly say "No critical skills missing.")
5. Specific Improvement Suggestions (If none, explicitly say "No significant improvements needed.")

Be honest and do not invent issues just to fill sections.

Resume:
{resume_text}
"""
    response = llm.invoke(prompt)
    if hasattr(response, "content"):
      return response.content
    return response