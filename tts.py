import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text to Speech", layout="centered")

# Header HTML (Made by is white, slightly moved up, slightly transparent)
header_html = (
    "<h1 style='color: #FFB13B; text-align: center; margin-bottom: 5px;'>"
    "🎙️TEXT TO SPEECH🎙️"
    "</h1>"
    "<p style='text-align: center; font-size: 12px; color: rgba(255,255,255,0.75); margin-top: -08px;'>"
    "Made by <b>PURWANSH CHAUDHARY</b>"
    "</p>"
)
st.markdown(header_html, unsafe_allow_html=True)

# Input
user_input = st.text_input("Type anything:")

if st.button("CONVERT"):
    if user_input.strip():
        tts = gTTS(user_input, lang='en')
        # save to a temporary file (avoids permission issues)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp_path = tmp.name
        tts.save(tmp_path)

        # play audio
        with open(tmp_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

        # cleanup temp file
        try:
            os.remove(tmp_path)
        except Exception:
            pass
    else:
        st.warning("Please enter some text!")

# Footer CSS + HTML (footer text white; name has slow 'breathing' red glow)
css_lines = [
    "<style>",
    ".footer {",
    "  position: fixed;",
    "  left: 0;",
    "  bottom: 0;",
    "  width: 100%;",
    "  text-align: center;",
    "  font-size: 12px;",
    "  color: white;",
    "  padding: 10px;",
    "  background: transparent;",
    "  pointer-events: none;",  # allows clicks through the footer
    "}",
    ".footer span { pointer-events: auto; }",
    ".glow {",
    "  color: red;",
    "  font-weight: bold;",
    "  animation: breathing 3s ease-in-out infinite;",
    "}",
    "@keyframes breathing {",
    "  0% { text-shadow: 0 0 5px red, 0 0 10px darkred; }",
    " 50% { text-shadow: 0 0 20px red, 0 0 40px darkred; }",
    " 100% { text-shadow: 0 0 5px red, 0 0 10px darkred; }",
    "}",
    "</style>",
]
css = "\n".join(css_lines)

footer_html = (
    "<div class='footer'>"
    "© 2025 Text to Speech Converter Project | Design by "
    "<span class='glow'>PURWANSH CHAUDHARY</span> | Made with ❤️ in Python & Streamlit"
    "</div>"
)

st.markdown(css + footer_html, unsafe_allow_html=True)






