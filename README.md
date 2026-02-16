# CareerPilot AI 🚀

CareerPilot AI is a web app that helps users improve their resume, compare it to a job description, and practice mock interviews using a local LLM.

Built with Python, Ollama (LLaMA 3), LangChain, and Streamlit.


---

## 🔗 Live Demo

[Add your deployment link here]

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

1. Install dependencies:

```bash
pip install -r requirements.txt
```
2.Start Ollama:
```bash
ollama run llama3
```

3.Run the app:
```bash
streamlit run app.py
```

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

Built as a personal portfolio project to demonstrate practical LLM application development, prompt design, and conversational AI workflows.
