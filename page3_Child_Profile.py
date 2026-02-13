import streamlit as st

st.title("🧒 Child Profile")

if not st.session_state.get("logged_in"):
    st.warning("Please login first.")
    st.stop()

st.subheader("🎯 Learning Progress")

st.metric("Math", "70%")
st.metric("Reading", "40%")
st.metric("Science", "55%")

st.progress(0.6)

st.subheader("🏆 Badges")
st.write("⭐ ⭐ 🏅")
