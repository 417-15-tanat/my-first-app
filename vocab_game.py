import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start_time = time.time()
    st.session_state.is_submitted = False

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, time_taken):
    st.balloons()
    score = 0
    answers = [ans1.strip().lower(), ans2.strip().lower(), ans3.strip().lower(), ans4.strip().lower()]
    correct = ["apple", "fish", "dog", "book"]
    for i, (answer, expected) in enumerate(zip(answers, correct), 1):
        if answer == expected:
            st.success(f"✅ ข้อ {i}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ {i}: ยังไม่ถูกต้อง (คุณตอบ '{answer}')")
    st.divider()
    st.metric(label="🏆 คะแนนที่ได้", value=f"{score} / 4")
    st.info(f"⏱️ เวลาที่ใช้: **{time_taken:.2f}** วินาที")
    if st.button("🔄 เล่นใหม่อีกครั้ง", use_container_width=True):
        reset_game()
        st.rerun()

st.write("กรุณาเติมคำศัพท์ภาษาอังกฤษให้ถูกต้องโดยเร็วที่สุด!")
ans1 = st.text_input("1. คำศัพท์แปลว่า 'แอปเปิ้ล':", key="ans1_val")
ans2 = st.text_input("2. คำศัพท์แปลว่า 'ปลา':", key="ans2_val")
ans3 = st.text_input("3. คำศัพท์แปลว่า 'สุนัข':", key="ans3_val")
ans4 = st.text_input("4. คำศัพท์แปลว่า 'หนังสือ':", key="ans4_val")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 ส่งคำตอบ", type="primary", use_container_width=True):
        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.is_submitted = True
        show_result_dialog(ans1, ans2, ans3, ans4, elapsed_time)
with col2:
    if st.button("🔄 เริ่มเกมใหม่", use_container_width=True):
        reset_game()
        st.rerun()
