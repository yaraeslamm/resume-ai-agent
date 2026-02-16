import streamlit as st
from resume_parser import extract_text_from_pdf
from resume_analyzer import analyze_resume
from job_matcher import analyze_job_match
from interview_agent import create_interview_chain
from audio_recorder_streamlit import audio_recorder
from voice_utils import transcribe_audio_bytes, generate_tts
import asyncio


st.title("📄 Resume Intelligence Agent")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        analysis = analyze_resume(resume_text)

    st.subheader("📊 Resume Analysis")
    st.write(analysis)


st.divider()
st.header("🎯 Job Match Analysis")

job_description = st.text_area("Paste Job Description Here")

if uploaded_file is not None and job_description:
    with st.spinner("Analyzing job match..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        similarity_score, match_analysis = analyze_job_match(resume_text, job_description)

    st.subheader("🔎 Semantic Similarity Score")
    st.write(f"{round(similarity_score * 100, 2)}%")

    st.subheader("📈 Detailed Match Analysis")
    st.write(match_analysis)

st.divider()
st.header("🎤 Interview Coach")

target_role = st.text_input("Target Role (Optional)")
experience_level = st.selectbox(
    "Experience Level",
    ["Entry-Level", "Mid-Level", "Senior-Level"]
)

if "interview_chain" not in st.session_state:
    st.session_state.interview_chain = None

if st.button("Start Interview"):
    st.session_state.interview_chain = create_interview_chain(
        job_description=job_description,
        target_role=target_role,
        experience_level=experience_level
    )
    first_question = st.session_state.interview_chain.predict(input="Start the interview.")
    st.write(first_question)

if st.session_state.interview_chain:
    user_answer = st.text_input("Your Answer:")

    if st.button("Submit Answer") and user_answer:
        response = st.session_state.interview_chain.predict(input=user_answer)
        st.write(response)



st.subheader("🎙 Record Your Answer")
if "history" not in st.session_state:
    st.session_state.history = []

for role, message in st.session_state.history:
    if role == "Interviewer":
        st.markdown(f"**🎤 Interviewer:**\n{message}")
    else:
        st.markdown(f"**🧑 You:** {message}")

audio = audio_recorder("Start Recording", "Stop Recording")
# st.write(audio) 
if audio is not None and len(audio) > 0 and st.session_state.interview_chain:
    # st.write(audio) 
    # st.audio(audio.export().read())
    st.audio(audio, format="audio/wav")

    # audio_bytes = audio, format="audio/wav"
    user_text = transcribe_audio_bytes(audio)

    st.write(f"📝 Transcribed: {user_text}")

    response = st.session_state.interview_chain.predict(input=user_text)

    # st.write(response)

    # speak_text(response)
    # Split question from feedback
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
    


# audio_input = st.file_uploader("Upload Audio Answer (wav/mp3)", type=["wav", "mp3"])

# if audio_input and st.session_state.interview_chain:
#     user_text = transcribe_audio(audio_input)
#     st.write(f"You said: {user_text}")

#     response = st.session_state.interview_chain.predict(input=user_text)

#     st.write(response)

#     speak_text(response)







# if "conversation" not in st.session_state:
#     st.session_state.conversation = []

# if st.button("Start Interview"):
#     st.session_state.conversation = []
#     first_question = generate_interview_response([])
#     st.session_state.conversation.append(("Interviewer", first_question))

# if st.session_state.conversation:
#     for role, message in st.session_state.conversation:
#         st.write(f"**{role}:** {message}")

#     user_answer = st.text_input("Your Answer:")

#     if st.button("Submit Answer") and user_answer:
#         st.session_state.conversation.append(("Candidate", user_answer))

#         response = generate_interview_response(st.session_state.conversation)

#         st.session_state.conversation.append(("Interviewer", response))

#         st.rerun()


