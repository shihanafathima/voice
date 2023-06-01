

import streamlit as st
import whisper

st.title("Speech to text")
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "mp4"])

model = whisper.load_model("base")
st.text("whisper model loader")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcricing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.side.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)