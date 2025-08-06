import streamlit as st

with open("tram_from_shuk") as file:
  html_code = file.read()

st.components.v1.html(html_code, height=800)
