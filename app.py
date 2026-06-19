import streamlit as st
import streamlit.components.v1 as components

# Set the page to full width
st.set_page_config(layout="wide")

st.sidebar.title("Navigation & Design")

# เพิ่มเมนูรวมเลเยอร์หน้า "ระบบของเรา" เข้าไปในระบบช้อยส์
selected_page = st.sidebar.radio(
    "เลือกหน้าเว็บที่ต้องการตรวจ:",
    (
        "หน้าแรก - สไตล์ที่ 1 (Original)", 
        "หน้าแรก - สไตล์ที่ 2 (Premium Blue)", 
        "หน้าแรก - สไตล์ที่ 3 (SaaS Clean)",
        "หน้าแรก - สไตล์ที่ 4 (Immersive Split Grid)",
        "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 1" ,
        "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 2",
        "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 3",
        "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 4"
    )
)

# แมปช้อยส์เข้าหาไฟล์ html ในเครื่อง
if selected_page == "หน้าแรก - สไตล์ที่ 1 (Original)":
    file_to_open = "index.html"
elif selected_page == "หน้าแรก - สไตล์ที่ 2 (Premium Blue)":
    file_to_open = "index2.html"
elif selected_page == "หน้าแรก - สไตล์ที่ 3 (SaaS Clean)":
    file_to_open = "index3.html"
elif selected_page == "หน้าแรก - สไตล์ที่ 4 (Immersive Split Grid)":
    file_to_open = "index4.html"
elif selected_page == "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 2":
    file_to_open = "our-services2.html"
elif selected_page == "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 3":
    file_to_open = "our-services3.html"
elif selected_page == "หน้ารายละเอียด - ระบบของเรา (Services) สไตล์ที่ 4":
    file_to_open = "our-services4.html"
else:
    file_to_open = "our-services.html" # 👈 วิ่งไปเปิดไฟล์นี้ทันที

# อ่านและเรนเดอร์เนื้อหา
try:
    with open(file_to_open, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # ปรับความสูงเพิ่มเป็น 1500 เผื่อหน้าระบบของเรามีรายละเอียดฟีเจอร์ค่อนข้างยาวครับ
    components.html(html_content, height=1500, scrolling=True)

except FileNotFoundError:
    st.error(f"❌ ไม่พบไฟล์ '{file_to_open}' ในโฟลเดอร์ กรุณาเช็คชื่อไฟล์อีกครั้งครับ")