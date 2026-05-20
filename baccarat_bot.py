import streamlit as st

st.set_page_config(page_title="Boss Baccarat", page_icon="🔴")
st.title("🔴 BOSS BACCARAT 🔵")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1

base_money = st.sidebar.number_input("Tien cuoc 1 don vi (VND):", min_value=1000, value=50000, step=10000)

fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
current_multiplier = fibo[st.session_state.current_step - 1]
suggested_bet = current_multiplier * base_money

st.subheader("🤖 Goiy lenh tiep theo:")
st.metric(label="So tien can danh", value=f"{suggested_bet:,} VND")

if len(st.session_state.history) >= 2:
    last = st.session_state.history[-1]
    prev = st.session_state.history[-2]
    if last == prev:
        st.write(f"👉 Nen danh: **{last}** (Cau Bet)")
    else:
        next_op = "PLAYER" if last == "BANKER" else "BANKER"
        st.write(f"👉 Nen danh: **{next_op}** (Cau Nhay)")
else:
    st.info("Nhap thieu 2 tay de bot phan tich")

st.subheader("📥 Nhap ket qua ban choi")
if st.button("🔴 BANKER"):
    st.session_state.history.append("BANKER")
    st.rerun()
if st.button("🔵 PLAYER"):
    st.session_state.history.append("PLAYER")
    st.rerun()
if st.button("🟢 TIE (Hoa)"):
    st.session_state.history.append("TIE")
    st.rerun()

st.subheader("💰 Xac nhan de len tien")
if st.button("✅ THANG LENH"):
    if st.session_state.current_step < len(fibo):
        st.session_state.current_step += 1
    st.rerun()
if st.button("❌ THUA LENH"):
    st.session_state.current_step = 1
    st.rerun()

if st.session_state.history:
    st.write(f"Lich su cau: {', '.join(st.session_state.history[-10:])}")
    if st.button("Reset Bot"):
        st.session_state.history = []
        st.session_state.current_step = 1
        st.rerun()
