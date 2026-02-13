import streamlit as st

st.title("📚 Learn")

subject = st.selectbox("Choose Subject", ["Math", "Reading", "Science", "Art"])

if subject == "Math":
    st.write("What is 7 + 5?")
    ans = st.radio("Choose:", ["10", "11", "12"])
    if st.button("Submit"):
        st.success("Correct!") if ans == "12" else st.error("Try again!")

elif subject == "Reading":
    st.write("Read this sentence: The cat sat on the mat.")

elif subject == "Science":
    st.write("The Earth goes around the Sun.")

elif subject == "Art":
    idea = st.text_input("What will you draw?")
    st.info(f"Draw a {idea or 'rainbow dragon'} 🐉")
