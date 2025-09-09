import streamlit as st
from gtts import gTTS
import os

st.title("Text to Speech App 🎤")

user_input = st.text_input("Enter anything:")

if st.button("Submit"):
    if user_input.strip() != "":
        tts = gTTS(user_input, lang='en')
        tts.save("speech.mp3")

        # Play audio in browser
        audio_file = open("speech.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("Please enter some text!")
