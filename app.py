import streamlit as st

with open("track_from_shuk.html") as file:
  html_code = file.read()

st.components.v1.html(html_code, height=800)
