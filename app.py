import streamlit as st

st.set_page_config(layout="wide")

# Список файлов для выбора
files = {
    "Трек до Щукинской (train)": "track_to_shuk.html",
    "Трек от Щукинской (val/test)": "track_from_shuk.html",
}

# Виджет для выбора файла
selected_file = st.selectbox("Выберите трек:", list(files.keys()))

# Чтение и отображение выбранного файла
with open(files[selected_file], "r", encoding="utf-8") as file:
    html_code = file.read()

st.components.v1.html(html_code, height=900, width=1600)
