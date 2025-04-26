import streamlit as st

st.set_page_config(page_title="Learning Assistant")

st.title("Welcome to Lerno")

video_file = open('media/videos/main/1080p60/ArrayExplanation.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
