import streamlit as st
import pandas as pd
import bcrypt
import os

st.set_page_config(page_title="Login - BrightKids")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Load users.csv safely
if os.path.exists("users.csv"):
    users = pd.read_csv("users.csv")
else:
    st.error("User database not found. Please add users.csv.")
    users = pd.DataFrame(columns=["email","password","role"])

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

# ✅ Role-based navigation check
if st.session_state.logged_in:
    if st.session_state.role == "Parent":
        st.switch_page("pages/parent_dashboard.py")
    elif st.session_state.role == "Child":
        st.switch_page("pages/child_profile.py")

