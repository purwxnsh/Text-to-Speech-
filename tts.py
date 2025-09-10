import streamlit as st
from gtts import gTTS
import os

# ----------------- Custom Heading -----------------
st.markdown(
    """
    <h1 style='color: red; text-align: center;'>
        TEXT TO SPEECH 🎙️
    </h1>
    <p style='text-align: center; font-size: 12px; color: rgba(0,0,0,0.6);'>
        Made by <b>PURWANSH CHAUDHARY</b>
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------- Text Input Section -----------------
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

# ----------------- Footer -----------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 12px;
        color: rgba(0,0,0,0.6);
        padding: 10px;
        background: white;
    }
    .glow {
        color: red;
        text-shadow: 0 0 5px red, 0 0 10px red, 0 0 20px darkred;
        font-weight: bold;
    }
    </style>
    <div class="footer">
        © 2025 Text to Speech Converter Project | Design by 
        <span class="glow">PURWANSH CHAUDHARY</span> | Made with ❤️ in Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

