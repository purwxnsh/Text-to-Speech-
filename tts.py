import streamlit as st
from gtts import gTTS
import os

# ----------------- Custom Heading -----------------
st.markdown("""
    <h1 style='color: red; text-align: center; margin-bottom: 5px;'>
        TEXT TO SPEECH 🎙️
    </h1>
    <p style='text-align: center; font-size: 12px; color: rgba(255,255,255,0.7); margin-top: -10px;'>
        Made by <b>PURWANSH CHAUDHARY</b>
    </p>
    """, unsafe_allow_html=True)

# ----------------- Text Input Section -----------------
user_input = st.text_input("Enter anything:")

if st.button("Submit"):
    if user_input.strip() != "":
        tts = gTTS(user_input, lang='en')
        tts.save("speech.mp3")

        # Play audio in browser
        with open("speech.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("Please enter some text!")

# ----------------- Footer -----------------
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        widt
