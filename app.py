import streamlit as st

st.set_page_config(page_title="BrightKids", page_icon="🌈", layout="centered")

# ---- App State ----
if "page" not in st.session_state:
    st.session_state.page = "home"
if "stars" not in st.session_state:
    st.session_state.stars = 0

# ---- Styling ----
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #1f6feb, #2ea043);
    color: white;
    padding: 32px;
    border-radius: 20px;
    margin-bottom: 24px;
}
.card {
    background: #f7f9fc;
    padding: 16px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
}
.small {
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# ---- Navigation Helper ----
def go(page):
    st.session_state.page = page

# ---- HOME PAGE ----
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <span>✨ New</span>
        <h1>BrightKids</h1>
        <p>Fun lessons, games, and an AI tutor for children aged 6–12.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📚 Explore Subjects")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown('<div class="card">➕<br><b>Math</b></div>', unsafe_allow_html=True)
        st.button("Start Math", on_click=go, args=("math",))

    with c2:
        st.markdown('<div class="card">📖<br><b>Reading</b></div>', unsafe_allow_html=True)
        st.button("Start Reading", on_click=go, args=("reading",))

    with c3:
        st.markdown('<div class="card">🔬<br><b>Science</b></div>', unsafe_allow_html=True)
        st.button("Start Science", on_click=go, args=("science",))

    with c4:
        st.markdown('<div class="card">🎨<br><b>Art</b></div>', unsafe_allow_html=True)
        st.button("Start Art", on_click=go, args=("art",))

    st.divider()
    st.markdown("### ⭐ Your Progress")
    st.write(f"Stars earned: {'⭐' * st.session_state.stars if st.session_state.stars else 'No stars yet'}")

# ---- MATH PAGE ----
elif st.session_state.page == "math":
    st.markdown("## 🧮 Math Lesson")
    q = st.radio("What is 8 + 4?", ["10", "11", "12", "13"])
    if st.button("Check answer"):
        if q == "12":
            st.success("Correct! ⭐ You earned a star!")
            st.session_state.stars += 1
        else:
            st.error("Oops, try again!")

    st.button("⬅️ Back to Home", on_click=go, args=("home",))

# ---- READING PAGE ----
elif st.session_state.page == "reading":
    st.markdown("## 📖 Reading Time")
    st.write("Once upon a time, a curious little fox learned how to read...")
    st.button("⬅️ Back to Home", on_click=go, args=("home",))

# ---- SCIENCE PAGE ----
elif st.session_state.page == "science":
    st.markdown("## 🔬 Science Fun Fact")
    st.info("🌍 The Earth goes around the Sun once every year!")
    st.button("⬅️ Back to Home", on_click=go, args=("home",))

# ---- ART PAGE ----
elif st.session_state.page == "art":
    st.markdown("## 🎨 Art Corner")
    idea = st.text_input("What would you like to draw today?")
    if st.button("Get idea"):
        st.success(f"Try drawing a {idea or 'rainbow unicorn'} 🦄🌈")
    st.button("⬅️ Back to Home", on_click=go, args=("home",))

# --- Mini Lesson ---
st.markdown("## 🧠 Today’s Mini Lesson (Math)")
st.write("What is **7 + 5**?")

answer = st.radio("Choose one:", ["10", "11", "12", "13"], key="quiz1")

if st.button("Check answer"):
    if answer == "12":
        st.success("🎉 Correct! Great job!")
    else:
        st.error("❌ Not quite. Try again!")

st.divider()

# --- AI Tutor ---
st.markdown("## 🤖 Ask the AI Tutor")
st.caption("Ask a question and the AI will explain in kid-friendly language.")

question = st.text_input("Ask a question (e.g., What is multiplication?)")

if st.button("Ask Tutor"):
    if question:
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"Explain this to a 9-year-old in simple, friendly language: {question}"
            )
            st.info(response.output_text)
    else:
        st.warning("Type a question first!")

st.divider()

# --- Progress ---
st.markdown("## ⭐ Your Progress")
st.progress(0.4)
st.write("Badges earned: 🏅 🏅")
st.write("Stars: ⭐⭐⭐")





# ---- FOOTER ----
st.divider()
st.caption("© 2026 BrightKids • Learn with joy 💙")



