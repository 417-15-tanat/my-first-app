import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าข้อ 2
    st.session_state.start_time = time.time()  # รีเซ็ตเวลา
    st.session_state.is_submitted = False  # รีเซ็ตสถานะส่งคำตอบ


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, time_taken):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # ตรวจข้อ 1 (โจทย์: ผลไม้สีแดง เช่น apple)
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2 (โจทย์: สัตว์ว่ายน้ำ เช่น fish)
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    st.divider()
    st.metric(label="🏆 คะแนนที่ได้", value=f"{score} / 2")
    st.info(f"⏱️ เวลาที่ใช้: **{time_taken:.2f}** วินาที")

    if st.button("🔄 เล่นใหม่อีกครั้ง", use_container_width=True):
        reset_game()
        st.rerun()


# ----------------------------------------------------
# 📌 ส่วนแสดงผล UI หน้าเว็บ
# ----------------------------------------------------
st.write("กรุณาเติมคำศัพท์ภาษาอังกฤษให้ถูกต้องโดยเร็วที่สุด!")

# ช่องกรอกคำตอบ
ans1 = st.text_input("1. คำศัพท์แปลว่า 'แอปเปิ้ล':", key="ans1_val")
ans2 = st.text_input("2. คำศัพท์แปลว่า 'ปลา':", key="ans2_val")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 ส่งคำตอบ", type="primary", use_container_width=True):
        # คำนวณเวลาที่ใช้
        elapsed_time = time.time() - st.session_state.start_time
        # เรียกเปิด Dialog สรุปผล
        show_result_dialog(ans1, ans2, elapsed_time)

with col2:
    if st.button("🔄 เริ่มเกมใหม่", use_container_width=True):
        reset_game()
        st.rerun()
