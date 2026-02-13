
import streamlit as st

# Protect Child Profile
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first.")
    st.stop()

if st.session_state.role != "Child":
    st.error("Access denied. This page is for Children only.")
    st.stop()

st.title("🧒 Child Profile")
st.write("Welcome to the Child Profile!")

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

