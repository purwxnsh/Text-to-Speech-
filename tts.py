import pyttsx3 
import streamlit as s
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',70)
user_input = s.text_input("enter anything")
if s.button('submit'):
 engine.say(user_input)
 engine.runAndWait()