import streamlit as st
from gtts import gTTS
import pyttsx3
import tempfile
import os

st.set_page_config(page_title="TTS Studio", layout="centered")

# ----------------- Custom CSS -----------------
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #1e1e2f, #2c3e50, #3a1c71, #2c5364);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff1a1a;
    transform: scale(1.05);
}
.audio-container {
    text-align: center;
    margin-top: 20px;
}
.glow {
    font-size: 14px;
    color: red;
    text-align: center;
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 5px red; }
    to { text-shadow: 0 0 20px red, 0 0 30px crimson; }
}
</style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown(
    "<h1 style='color: #F5B727; text-align: center; margin-bottom: 5px;'>🎙️TEXT TO SPEECH🎙️</h1>"
    "<p style='text-align: center; font-size: 12px; color: rgba(255,255,255,0.7); margin-top: -10px;'>"
    "Made by <span class='glow'>PURWANSH CHAUDHARY</span></p>",
    unsafe_allow_html=True
)

# ----------------- Text Input -----------------
st.markdown("### ✍️ Enter Text")
user_input = st.text_area("Type here:", placeholder="Example: Hi, My my name is Purav ")

# ----------------- Language Selection -----------------
language = st.selectbox("🌍 Select Language", [
    ("English", "en"), 
    ("Hindi", "hi"), 
    ("French", "fr"), 
    ("Spanish", "es"), 
    ("German", "de")
], format_func=lambda x: x[0])

# ----------------- Engine Selection -----------------
engine_choice = st.radio("🎤 Voice Engine", ["gTTS (Google, Online)", "pyttsx3 (Offline)"])

# ----------------- pyttsx3 Options -----------------
if engine_choice == "pyttsx3 (Offline)":
    st.markdown("### 🎛️ Voice Settings")
    gender = st.radio("Select Voice Type:", ["Male", "Female"])
    speed = st.slider("Adjust Speech Speed:", min_value=50, max_value=300, value=150, step=10)

# ----------------- Convert to Speech -----------------
if st.button("🔊 Convert to Speech"):
    if user_input.strip():
        if engine_choice.startswith("gTTS"):
            # Online TTS
            lang_code = language[1]
            tts = gTTS(user_input, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tmp_path = tmp.name
            tts.save(tmp_path)
        else:
            # Offline TTS using pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")

            # Set gender
            if gender == "Male":
                engine.setProperty("voice", voices[0].id)
            else:
                if len(voices) > 1:
                    engine.setProperty("voice", voices[1].id)

            # Set speech speed
            engine.setProperty("rate", speed)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tmp_path = tmp.name
            engine.save_to_file(user_input, tmp_path)
            engine.runAndWait()

        # ----------------- Audio Player -----------------
        st.markdown("<div class='audio-container'><h4>🔊 Your Speech Output</h4></div>", unsafe_allow_html=True)
        with open(tmp_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

            # ----------------- Download Button -----------------
            st.download_button(
                label="⬇️ Download MP3",
                data=audio_bytes,
                file_name="speech.mp3",
                mime="audio/mp3"
            )

        # Cleanup temp file
        try:
            os.remove(tmp_path)
        except Exception:
            pass
    else:
        st.warning("Please enter some text!")

# ----------------- Footer -----------------
st.markdown("""
<style>
.footer {
    text-align: center;
    font-size: 12px;
    color: white;
    margin-top: 50px;
    opacity: 0.8;
}
.glow-red {
    color: red;
    font-weight: bold;
    animation: glow 2s ease-in-out infinite alternate;
}
</style>
<div class="footer">
    © 2025 Text to Speech Converter Project | Design by 
    <span class="glow-red">PURWANSH CHAUDHARY</span> | Made with ❤️ in Python & Streamlit
</div>
""", unsafe_allow_html=True)

