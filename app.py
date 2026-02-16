# import streamlit as st
# from resume_parser import extract_text_from_pdf
# from resume_analyzer import analyze_resume
# from job_matcher import analyze_job_match
# from interview_agent import create_interview_chain
# from audio_recorder_streamlit import audio_recorder
# from voice_utils import transcribe_audio_bytes, generate_tts
# import asyncio

# st.set_page_config(
#     page_title="CareerPilot AI",
#     page_icon="🚀",
#     layout="wide"
# )

# st.title("🚀 CareerPilot AI")
# st.subheader("LLM-Powered Resume & Interview Optimization Platform")

# st.markdown("---")

# st.markdown("""
# ### 🧠 What This Platform Does

# CareerPilot AI helps you:

# - Analyze your resume using AI evaluation
# - Match your resume against job descriptions
# - Identify missing skills and alignment gaps
# - Simulate real technical interviews
# - Receive structured feedback and refined answer examples

# Designed to provide realistic, structured, and improvement-focused guidance.
# """)

# st.markdown("---")

# # Feature Sections
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("## 📄 Resume Analyzer")
#     st.markdown("""
# Upload your resume to receive:

# - Overall ATS-style evaluation
# - Strengths & weaknesses
# - Missing or weak skills
# - Concrete improvement suggestions

# 💡 *For best results, upload your most updated resume.*
# """)

# with col2:
#     st.markdown("## 🎯 Job Matching")
#     st.markdown("""
# Compare your resume against a job description to:

# - Measure alignment score
# - Identify missing skills
# - Highlight strengths
# - Improve targeting strategy

# ⚠ *Accuracy improves when resume is uploaded first.*
# """)

# with col3:
#     st.markdown("## 🎙 Interview Coach")
#     st.markdown("""
# Simulate a structured technical interview:

# - One question at a time
# - Adaptive difficulty
# - Structured feedback
# - Refined answer examples
# - Voice interaction enabled
# """)

# st.markdown("---")

# st.info("⚡ Tip: Upload your resume first for the most accurate job matching and interview personalization.")


# st.title("📄 Resume Intelligence Agent")

# uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# if uploaded_file is not None:
#     with st.spinner("Analyzing resume..."):
#         resume_text = extract_text_from_pdf(uploaded_file)
#         analysis = analyze_resume(resume_text)

#     st.subheader("📊 Resume Analysis")
#     st.write(analysis)


# st.divider()
# st.header("🎯 Job Match Analysis")

# job_description = st.text_area("Paste Job Description Here")

# if uploaded_file is not None and job_description:
#     with st.spinner("Analyzing job match..."):
#         resume_text = extract_text_from_pdf(uploaded_file)
#         similarity_score, match_analysis = analyze_job_match(resume_text, job_description)

#     st.subheader("🔎 Semantic Similarity Score")
#     st.write(f"{round(similarity_score * 100, 2)}%")

#     st.subheader("📈 Detailed Match Analysis")
#     st.write(match_analysis)

# st.divider()
# st.header("🎤 Interview Coach")

# target_role = st.text_input("Target Role (Optional)")
# experience_level = st.selectbox(
#     "Experience Level",
#     ["Entry-Level", "Mid-Level", "Senior-Level"]
# )

# if "interview_chain" not in st.session_state:
#     st.session_state.interview_chain = None

# if st.button("Start Interview"):
#     st.session_state.interview_chain = create_interview_chain(
#         job_description=job_description,
#         target_role=target_role,
#         experience_level=experience_level
#     )
#     first_question = st.session_state.interview_chain.predict(input="Start the interview.")
#     st.write(first_question)

# if st.session_state.interview_chain:
#     user_answer = st.text_input("Your Answer:")

#     if st.button("Submit Answer") and user_answer:
#         response = st.session_state.interview_chain.predict(input=user_answer)
#         st.write(response)



# st.subheader("🎙 Record Your Answer")
# if "history" not in st.session_state:
#     st.session_state.history = []

# for role, message in st.session_state.history:
#     if role == "Interviewer":
#         st.markdown(f"**🎤 Interviewer:**\n{message}")
#     else:
#         st.markdown(f"**🧑 You:** {message}")

# audio = audio_recorder("Start Recording", "Stop Recording")
# # st.write(audio) 
# if audio is not None and len(audio) > 0 and st.session_state.interview_chain:
#     # st.write(audio) 
#     # st.audio(audio.export().read())
#     st.audio(audio, format="audio/wav")

#     # audio_bytes = audio, format="audio/wav"
#     user_text = transcribe_audio_bytes(audio)

#     st.write(f"📝 Transcribed: {user_text}")

#     response = st.session_state.interview_chain.predict(input=user_text)

#     # st.write(response)

#     # speak_text(response)
#     # Split question from feedback
#     if "Question:" in response:
#         question_part = response.split("Question:")[1].split("Feedback:")[0].strip()
#     else:
#         question_part = ""

#     st.session_state.history.append(("Candidate", user_text))
#     st.session_state.history.append(("Interviewer", response))
#     if question_part:
#         audio_file = asyncio.run(generate_tts(question_part))
#         with open(audio_file, "rb") as f:
#             st.audio(f.read(), format="audio/mp3")
    


# # audio_input = st.file_uploader("Upload Audio Answer (wav/mp3)", type=["wav", "mp3"])

# # if audio_input and st.session_state.interview_chain:
# #     user_text = transcribe_audio(audio_input)
# #     st.write(f"You said: {user_text}")

# #     response = st.session_state.interview_chain.predict(input=user_text)

# #     st.write(response)

# #     speak_text(response)







# # if "conversation" not in st.session_state:
# #     st.session_state.conversation = []

# # if st.button("Start Interview"):
# #     st.session_state.conversation = []
# #     first_question = generate_interview_response([])
# #     st.session_state.conversation.append(("Interviewer", first_question))

# # if st.session_state.conversation:
# #     for role, message in st.session_state.conversation:
# #         st.write(f"**{role}:** {message}")

# #     user_answer = st.text_input("Your Answer:")

# #     if st.button("Submit Answer") and user_answer:
# #         st.session_state.conversation.append(("Candidate", user_answer))

# #         response = generate_interview_response(st.session_state.conversation)

# #         st.session_state.conversation.append(("Interviewer", response))

# #         st.rerun()

import streamlit as st
from resume_parser import extract_text_from_pdf
from resume_analyzer import analyze_resume
from job_matcher import analyze_job_match
from interview_agent import create_interview_chain
from audio_recorder_streamlit import audio_recorder
from voice_utils import transcribe_audio_bytes, generate_tts
import asyncio

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.title("🚀 CareerPilot AI")
st.subheader("LLM-Powered Resume & Interview Optimization Platform")
st.markdown("---")

st.markdown("""
### 🧠 What This Platform Does

CareerPilot AI helps you:

- Analyze your resume using AI evaluation
- Match your resume against job descriptions
- Identify missing skills and alignment gaps
- Simulate real technical interviews
- Receive structured feedback and refined answer examples

Designed to provide realistic, structured, and improvement-focused guidance.
""")

st.markdown("---")

# -------------------------------------------------
# FEATURE OVERVIEW (CLEAN GRID)
# -------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("## 📄 Resume Analyzer")
    st.markdown("""
- Overall ATS-style evaluation  
- Strengths & weaknesses  
- Missing or weak skills  
- Concrete improvement suggestions  

💡 *For best results, upload your most updated resume.*
""")

with col2:
    st.markdown("## 🎯 Job Matching")
    st.markdown("""
- Measure alignment score  
- Identify missing skills  
- Highlight strengths  
- Improve targeting strategy  

⚠ *Accuracy improves when resume is uploaded first.*
""")

with col3:
    st.markdown("## 🎙 Interview Coach")
    st.markdown("""
- One question at a time  
- Adaptive difficulty  
- Structured feedback  
- Refined answer examples  
- Voice interaction enabled
""")

st.info("⚡ Tip: Upload your resume first for the most accurate job matching and interview personalization.")

st.markdown("---")

# =================================================
# MAIN APPLICATION TABS
# =================================================
tab1, tab2, tab3 = st.tabs([
    "📄 Resume Intelligence Agent",
    "🎯 Job Match Analysis",
    "🎤 Interview Coach"
])

# =================================================
# TAB 1 — RESUME ANALYSIS
# =================================================
with tab1:
    st.header("📄 Resume Intelligence Agent")

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF)",
        type="pdf"
    )

    if uploaded_file is not None:
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            analysis = analyze_resume(resume_text)

        st.subheader("📊 Resume Analysis")
        st.write(analysis)

# =================================================
# TAB 2 — JOB MATCHING
# =================================================
with tab2:
    st.header("🎯 Job Match Analysis")

    job_description = st.text_area(
        "Paste Job Description Here",
        height=250
    )

    if uploaded_file is not None and job_description:
        with st.spinner("Analyzing job match..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            similarity_score, match_analysis = analyze_job_match(
                resume_text,
                job_description
            )

        col_score, col_analysis = st.columns([1, 2])

        with col_score:
            st.metric(
                "🔎 Semantic Similarity Score",
                f"{round(similarity_score * 100, 2)}%"
            )

        with col_analysis:
            st.subheader("📈 Detailed Match Analysis")
            st.write(match_analysis)

# =================================================
# TAB 3 — INTERVIEW COACH
# =================================================
with tab3:
    st.header("🎤 Interview Coach")

    col_left, col_right = st.columns(2)

    with col_left:
        target_role = st.text_input("Target Role (Optional)")

    with col_right:
        experience_level = st.selectbox(
            "Experience Level",
            ["Entry-Level", "Mid-Level", "Senior-Level"]
        )

    if "interview_chain" not in st.session_state:
        st.session_state.interview_chain = None

    if "history" not in st.session_state:
        st.session_state.history = []

    st.markdown("---")

    # START INTERVIEW
    if st.button("🚀 Start Interview"):
        st.session_state.interview_chain = create_interview_chain(
            job_description=job_description,
            target_role=target_role,
            experience_level=experience_level
        )
        first_question = st.session_state.interview_chain.predict(
            input="Start the interview."
        )
        st.write(first_question)

    # TEXT ANSWER FLOW
    if st.session_state.interview_chain:
        st.subheader("💬 Text Answer")

        user_answer = st.text_input("Your Answer:")

        if st.button("Submit Answer") and user_answer:
            response = st.session_state.interview_chain.predict(
                input=user_answer
            )
            st.write(response)

    st.markdown("---")
    st.subheader("🎙 Voice Interaction")

    # DISPLAY HISTORY
    for role, message in st.session_state.history:
        if role == "Interviewer":
            st.markdown(f"**🎤 Interviewer:**\n{message}")
        else:
            st.markdown(f"**🧑 You:** {message}")

    audio = audio_recorder("Start Recording", "Stop Recording")

    if (
        audio is not None
        and len(audio) > 0
        and st.session_state.interview_chain
    ):
        st.audio(audio, format="audio/wav")

        user_text = transcribe_audio_bytes(audio)
        st.write(f"📝 Transcribed: {user_text}")

        response = st.session_state.interview_chain.predict(
            input=user_text
        )

        if "Question:" in response:
            question_part = response.split("Question:")[1].split("Feedback:")[0].strip()
        else:
            question_part = ""

        st.session_state.history.append(("Candidate", user_text))
        st.session_state.history.append(("Interviewer", response))

        if question_part:
            audio_file = asyncio.run(generate_tts(question_part))
            with open(audio_file, "rb") as f:
                st.audio(f.read(), format="audio/mp3")

