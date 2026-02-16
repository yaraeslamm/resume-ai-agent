import streamlit as st
import whisper
import pyttsx3
import tempfile
import edge_tts
import asyncio

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()
# model = whisper.load_model("base") #speech to text
tts_engine = pyttsx3.init()   #text to speech

# def transcribe_audio(audio_file): # using temp file to handle the uploaded audio file as streamlit provides it as a file-like object
#     with tempfile.NamedTemporaryFile(delete=False) as tmp:
#         tmp.write(audio_file.read())
#         tmp_path = tmp.name
def transcribe_audio_bytes(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return result["text"]

# def speak_text(text):
#     tts_engine.say(text)
#     tts_engine.runAndWait()

async def generate_tts(text, output_file="response.mp3"):
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save(output_file)
    return output_file
