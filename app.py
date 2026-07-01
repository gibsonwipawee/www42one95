from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).parent

STYLE_FILES = {
    "Style 1 - Original": ROOT / "style1" / "index.html",
    "Style 2 - Premium Blue": ROOT / "style2" / "index2.html",
    "Style 3 - SaaS Clean": ROOT / "style3" / "index3.html",
    "Style 4 - Immersive Split Grid": ROOT / "style4" / "index4.html",
}

st.set_page_config(page_title="42one95 Style Preview", layout="wide")
st.sidebar.title("42one95 Styles")

selected_style = st.sidebar.radio(
    "เลือกสไตล์ที่ต้องการตรวจ:",
    tuple(STYLE_FILES.keys()),
)

file_to_open = STYLE_FILES[selected_style]

try:
    html_content = file_to_open.read_text(encoding="utf-8")
    base_tag = f'<base href="{file_to_open.parent.as_uri()}/">'
    html_content = html_content.replace("<head>", f"<head>\n    {base_tag}", 1)
    components.html(html_content, height=3200, scrolling=True)
except FileNotFoundError:
    st.error(f"ไม่พบไฟล์ {file_to_open}")
