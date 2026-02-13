import streamlit as st

st.set_page_config(page_title="Login - BrightKids")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
role = st.radio("Login as:", ["Parent", "Child"])

if st.button("Login"):
    if email and password:
        st.session_state.logged_in = True
        st.session_state.role = role
        st.success(f"Logged in as {role}")
    else:
        st.error("Please enter login details")

if st.session_state.logged_in:
    st.info("You are logged in. Use sidebar to navigate.")
