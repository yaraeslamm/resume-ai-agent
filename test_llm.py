from langchain_community.llms import Ollama


llm = Ollama(model="llama3")

response = llm.invoke("Explain what a resume is in 2 lines.")
print(response)
