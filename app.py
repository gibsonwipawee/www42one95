import streamlit as st
import streamlit.components.v1 as components

# Set the page to full width
st.set_page_config(layout="wide")

# สร้าง Sidebar สำหรับให้กดเลือกเวอร์ชันของหน้าเว็บ
st.sidebar.title("🎨 Design Version")
selected_version = st.sidebar.radio(
    "เลือกดูดีไซน์หน้าแรก:",
    ("Version 1 (Original Style)", "Version 2 (Premium Dark Blue)")
)

# คัดเลือกไฟล์ตามที่ผู้ใช้กดเลือกบน Sidebar
if selected_version == "Version 1 (Original Style)":
    file_to_open = "index.html"
else:
    file_to_open = "index2.html"

# อ่านไฟล์ HTML ที่ถูกเลือก
try:
    with open(file_to_open, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # เรนเดอร์ไฟล์ HTML ออกมาบนสตรีมลิต (ปรับความสูงเป็น 1200 หรือตามต้องการให้เห็นชัด ๆ)
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error(f"❌ ไม่พบไฟล์ '{file_to_open}' กรุณาตรวจสอบว่าวางไฟล์ไว้ในโฟลเดอร์เดียวกันแล้วหรือยัง")