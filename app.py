import streamlit as st

st.set_page_config(page_title="BrightKids")

# Initialize session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If not logged in → redirect to login page
if not st.session_state.logged_in:
    st.switch_page("pages/1_login.py")

# Main homepage (only visible after login)
st.title("🎓 BrightKids Learning Platform")
st.write("Welcome to BrightKids!")



