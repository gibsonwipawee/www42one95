import streamlit as st
import streamlit.components.v1 as components

# Set the page to full width
st.set_page_config(layout="wide")

# สร้าง Sidebar สำหรับให้กดเลือกเวอร์ชันของหน้าเว็บ (เพิ่มเป็น 3 ตัวเลือก)
st.sidebar.title("🎨 Design Version")
selected_version = st.sidebar.radio(
    "เลือกดูดีไซน์หน้าแรก:",
    (
        "Version 1 (Original Style)", 
        "Version 2 (Premium Dark Blue)", 
        "Version 3 (Tech-SaaS Automation)"
    )
)

# จับคู่ตัวเลือกกับชื่อไฟล์ HTML
if selected_version == "Version 1 (Original Style)":
    file_to_open = "index.html"
elif selected_version == "Version 2 (Premium Dark Blue)":
    file_to_open = "index2.html"
else:
    file_to_open = "index3.html"

# อ่านไฟล์ HTML ที่ถูกเลือกมาแสดงผล
try:
    with open(file_to_open, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # เรนเดอร์ไฟล์ HTML (ปรับความสูงเป็น 1200 เพื่อให้ดูได้เต็มอิ่ม)
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error(f"❌ ไม่พบไฟล์ '{file_to_open}' กรุณาตรวจสอบว่าวางไฟล์นี้ไว้ในโฟลเดอร์เดียวกับ app.py แล้วหรือยัง")