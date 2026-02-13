import streamlit as st

# Protect Parent Dashboard
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first.")
    st.stop()

if st.session_state.role != "Parent":
    st.error("Access denied. This page is for Parents only.")
    st.stop()

st.title("👨‍👩‍👧 Parent Dashboard")
st.write("Welcome to the Parent Dashboard!")

st.title("👨‍👩‍👧 Parent Dashboard")

if not st.session_state.get("logged_in") or st.session_state.get("role") != "Parent":
    st.warning("Please login as Parent to access this page.")
    st.stop()

st.subheader("👶 Child Profiles")

if "children" not in st.session_state:
    st.session_state.children = []

new_child = st.text_input("Add Child Name")

if st.button("Add Child"):
    if new_child:
        st.session_state.children.append(new_child)
        st.success(f"Added {new_child}")

st.write("Your Children:")
for child in st.session_state.children:
    st.markdown(f"- 🧒 {child}")

