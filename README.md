# CareerPilot AI 🚀

CareerPilot AI is a LLM-powered web application that helps users improve their resume, compare it to a job description, and practice mock interviews using a local LLM.

Built with Python, Ollama (LLaMA 3), LangChain, and Streamlit.


---

## 🔗 Deployment

### ✨ Live Demo

- 🖱️ **[Try It](https://resume-ai-agent-ibesnexhzmikbqmryfkg7i.streamlit.app)**  
 

- 🐳 **Dockerized production version:** Currently in progress…

---

### 🤖 Model Variants

- **Cloud Streamlit Demo:** Uses **Llama 3.1 8B Instant** via **Groq** hosted inference (optimized for fast, responsive interactions).
- **Docker Version:** Runs a local **LLaMA 3** model using **Ollama**.
- **Local Development:** Fully local execution powered by **Ollama** (see the [Run Locally](#-run-locally) section for setup instructions).



---


## Overview

CareerPilot AI supports three core workflows:

- **Resume Analysis** – Structured feedback on strengths, weaknesses, and improvement areas  
- **Job Description Matching** – Resume-to-job alignment scoring with skill gap insights  
- **Interview Simulation** – Adaptive mock interviews with feedback after each answer  

The system emphasizes structured outputs, controlled prompting, and non-hallucinated feedback.

---

## ✨ Features

### 📄 Resume Feedback
- Clear strengths and weaknesses
- Missing skills detection
- Practical improvement suggestions
- No invented experience or skills

### 🎯 Resume–Job Matching
- Similarity score between resume and job description
- Skill overlap analysis
- Suggestions to improve alignment

### 🎙 Interview Simulation
- Role-based mock interviews
- Optional experience level selection
- One question at a time
- Feedback after every answer:
  - Technical evaluation
  - Communication feedback
  - Improved sample answer
- Conversation memory during the session

---

## 🛠 Tech Stack

- Python  
- Ollama (LLaMA 3)  
- LangChain  
- Streamlit  

---

## 💻 Run Locally

Follow these steps to run the project locally using Ollama-based inference:

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start Ollama and Pull LLaMA 3

```bash
ollama run llama3
```

### 3️⃣ Update the LLM Configuration

Remove the Groq-related code and add:

```python
from langchain_community.llms import Ollama
```

Initialize the model:

```python
llm = Ollama(model="llama3")
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Your application should now be running locally with a fully local LLaMA 3 model powered by Ollama.

---

## 🔮 Future Improvements

- User progress tracking with authentication  
- Vector database integration (FAISS / Chroma) for RAG-based retrieval  
- Resume auto-tailoring per job description (LaTeX export support)  

---

## ⚠ Limitations

- LLM responses may vary slightly between sessions  
- Feedback quality depends on input quality  
- Not a replacement for real recruiters or interviewers  

---

## 👩‍💻 Author

Built with curiosity and care by **Yara Elshehawi** 🌱

🌐 [Portfolio](https://yaraeslamm.github.io)

🔗 [LinkedIn](https://www.linkedin.com/in/yara-eslam-877421212/)
