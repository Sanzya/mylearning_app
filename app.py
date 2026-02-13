import streamlit as st

st.set_page_config(page_title="BrightKids", page_icon="🌈", layout="centered")

# ---- App State ----
if "page" not in st.session_state:
    st.session_state.page = "home"
if "stars" not in st.session_state:
    st.session_state.stars = 0
if "badges" not in st.session_state:
    st.session_state.badges = []

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
</style>
""", unsafe_allow_html=True)

# ---- Navigation Helper ----
def go(page):
    st.session_state.page = page

# ---- HOME PAGE ----
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <h1>BrightKids 🌈</h1>
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
    st.markdown("### ⭐ Progress")
    st.write(f"Stars: {'⭐' * st.session_state.stars if st.session_state.stars else 'No stars yet'}")
    st.button("👨‍👩‍👧 Parent Dashboard", on_click=go, args=("parent",))

# ---- MATH PAGE ----
elif st.session_state.page == "math":
    st.markdown("## 🧮 Math Lesson")
    q = st.radio("What is 8 + 4?", ["10", "11", "12", "13"])
    if st.button("Check answer"):
        if q == "12":
            st.success("Correct! ⭐")
            st.session_state.stars += 1
            if "Math Star" not in st.session_state.badges:
                st.session_state.badges.append("Math Star 🧮")
        else:
            st.error("Try again!")

    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- READING PAGE ----
elif st.session_state.page == "reading":
    st.markdown("## 📖 Reading Time")
    st.write("Once upon a time, a little fox learned to read every day.")
    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- SCIENCE PAGE ----
elif st.session_state.page == "science":
    st.markdown("## 🔬 Science Fun Fact")
    st.info("The Sun is a star 🌟")
    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- ART PAGE ----
elif st.session_state.page == "art":
    st.markdown("## 🎨 Art Corner")
    idea = st.text_input("What would you like to draw?")
    if st.button("Get idea"):
        st.success(f"Try drawing a {idea or 'dragon flying over a castle'} 🐉🏰")
    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- DAILY CHALLENGE ----
elif st.session_state.page == "challenge":
    st.markdown("## 🧩 Daily Challenge")
    q = st.radio("What is 5 × 3?", ["10", "12", "15", "20"])
    if st.button("Submit"):
        if q == "15":
            st.success("Awesome! 🎉 You completed today's challenge!")
            st.session_state.stars += 2
        else:
            st.error("Oops! Try again tomorrow.")
    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- AI TUTOR (FREE MOCK) ----
elif st.session_state.page == "ai":
    st.markdown("## 🤖 AI Tutor")
    q = st.text_input("Ask a question")
    if st.button("Ask"):
        if q:
            st.info(f"Great question! Here's a simple answer: {q} means learning step by step with practice 😊")
    st.button("⬅️ Back", on_click=go, args=("home",))

# ---- PARENT DASHBOARD ----
elif st.session_state.page == "parent":
    st.markdown("## 👨‍👩‍👧 Parent Dashboard")
    st.metric("Stars Earned", st.session_state.stars)
    st.write("Badges:", ", ".join(st.session_state.badges) if st.session_state.badges else "No badges yet")
    st.progress(min(st.session_state.stars / 10, 1.0))
    st.button("⬅️ Back to Home", on_click=go, args=("home",))

# ---- Footer Navigation ----
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.button("🤖 AI Tutor", on_click=go, args=("ai",))
with c2:
    st.button("🧩 Daily Challenge", on_click=go, args=("challenge",))
with c3:
    st.button("🏆 Parent View", on_click=go, args=("parent",))
