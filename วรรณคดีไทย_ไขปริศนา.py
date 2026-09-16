import time
import streamlit as st

st.title("วรรณคดีไทย ไขปริศนา")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.ans6_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6):
    st.balloons()

    score = 0

    # แปลงคำตอบเป็นตัวพิมพ์เล็กและตัดช่องว่าง
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans4.strip().lower()
    u_ans6 = ans4.strip().lower()

    # ------------------------------------------------
    # ตรวจข้อ 1
    # ------------------------------------------------
    if u_ans1 == "พระอภัยมณี":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ------------------------------------------------
    # ตรวจข้อ 2
    # ------------------------------------------------
    if u_ans2 == "ขุนช้างขุนแผน":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ------------------------------------------------
    # ตรวจข้อ 3
    # ------------------------------------------------
    if u_ans3 == "รามเกียรติ์":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ------------------------------------------------
    # ตรวจข้อ 4
    # ------------------------------------------------
    if u_ans4 == "สังข์ทอง":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

   # ------------------------------------------------
    # ตรวจข้อ 5
    # ------------------------------------------------
    if u_ans5 == "อิเหนา":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

   # ------------------------------------------------
    # ตรวจข้อ 6
    # ------------------------------------------------
    if u_ans6 == "ไกรทอง":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")


    # ------------------------------------------------
    # แสดงคะแนนรวม
    # ------------------------------------------------
    st.info(f"🏆 ได้คะแนนรวม: {score} / 6 คะแนน")

    if score == 6:
        st.success("🎉 คุณชนะ")
    else:
        st.error("💀 คุณแพ้!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# ----------------------------------------------------
# 2. แถบแสดงเวลานับถอยหลัง
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(120 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 3. ช่องรับคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: เครื่องดนตรีสังหารยักษ์, การเดินทางกลางทะเล, ความรักต่างเผ่าพันธุ์ 🪈 🧜‍♀️ 🌊 👹 ",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "ข้อ 2: โศกนาฏกรรมหญิงสองใจ, การชิงรักหักสวาท, คดีความถึงกษัตริย์ ⚔️ 🪓 💔 📜",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "ข้อ 3: มหาศึกสงครามมนุษย์และยักษ์, กองทัพลิง, การลักพาตัวมเหสี 🏹 🐵 👹 👑",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "ข้อ 4: การเสี่ยงพวงมาลัยเลือกคู่, ร่างซ่อนรูปภายใต้ความน่ากลัว, การแข่งขันตีคลี 🐚 👺 💐 🏏",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    "ข้อ 5: ปฏิเสธการหมั้นตั้งแต่เด็ก, เผาเมืองลักพาตัวนางเอก, การรบเพื่อแย่งชิงบุษบา 🗡️ 🌺 🔥 💍",
    value=st.session_state.ans5_val,
)

ans6 = st.text_input(
    "ข้อ 6: หมอจระเข้ปราบชาละวัน, ถ้ำแก้วใต้บาดาล, ศึกเมียมนุษย์กับเมียจระเข้ 🐊 🔮 🗡️ 💎",
    value=st.session_state.ans6_val,
)


# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6


# ----------------------------------------------------
# 4. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 5. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6)


st.divider()

st.write("นางสาวดารารัตน์ นันทกุลพลพินิจ เลขที่ 4 ม.4/4")
