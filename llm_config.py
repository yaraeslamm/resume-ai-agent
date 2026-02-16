# from langchain_community.llms import Ollama

# llm = Ollama(model="llama3")

from langchain_community.chat_models import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 

llm = ChatGroq(
    temperature=0.3,
    model_name="llama3-70b-8192",
    groq_api_key=GROQ_API_KEY
)
