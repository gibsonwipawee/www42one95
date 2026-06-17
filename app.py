import streamlit as st
import streamlit.components.v1 as components

# Set the page to full width
st.set_page_config(layout="wide")

# Read the HTML file content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML string (adjust height/width as needed)
components.html(html_content, height=800, scrolling=True)