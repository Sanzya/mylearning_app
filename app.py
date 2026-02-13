import streamlit as st
import pandas as pd
import bcrypt

st.set_page_config(page_title="Login - BrightKids")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

users = pd.read_csv("users.csv")

def authenticate(email, password):
    user = users[users['email'] == email]
    if not user.empty:
        stored_pw = user.iloc[0]['password']
        role = user.iloc[0]['role']
        if bcrypt.checkpw(password.encode(), stored_pw.encode()):
            return role
    return None

if st.button("Login"):
    role = authenticate(email, password)
    if role:
        st.session_state.logged_in = True
        st.session_state.role = role
        st.success(f"Logged in as {role}")
    else:
        st.error("Invalid credentials")

if st.session_state.logged_in:
    st.info("You are logged in. Use sidebar to navigate.")

