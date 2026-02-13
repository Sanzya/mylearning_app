import streamlit as st

st.set_page_config(page_title="Login - BrightKids")

users = {
    "parent@example.com": {"password": "parent123", "role": "Parent"},
    "child@example.com": {"password": "child123", "role": "Child"}
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email in users and users[email]["password"] == password:
        st.session_state.logged_in = True
        st.session_state.role = users[email]["role"]
        st.success(f"Logged in as {st.session_state.role}")
    else:
        st.error("Invalid credentials")

if st.session_state.logged_in:
    st.info("You are logged in. Use sidebar to navigate.")

