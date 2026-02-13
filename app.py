import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv





# --- Setup ---
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="BrightKids – Learn with AI", page_icon="🌈", layout="centered")

# --- Styles ---
st.markdown("""
<style>
.hero {
  background: linear-gradient(135deg, #0b3c5d, #1f7ae0);
  padding: 4rem 2rem;
  border-radius: 20px;
  color: white;
  margin-bottom: 2rem;
}
.hero h1 { font-size: 42px; font-weight: 800; margin-bottom: 0.5rem; }
.hero p { font-size: 18px; max-width: 600px; }
.badge {
  display:inline-block; background:#111827; color:#fff; padding:6px 12px; border-radius:999px; font-size:12px;
}
.card {
  background:white; padding:20px; border-radius:16px; box-shadow:0 8px 24px rgba(0,0,0,0.06); text-align:center;
}
.cta button {
  background:white; color:#0b3c5d; border-radius:12px; padding:12px 18px; font-weight:700; border:none;
}
</style>
""", unsafe_allow_html=True)

# --- Hero ---
st.markdown("""
<div class="hero">
  <span class="badge">✨ New</span>
  <h1>BrightKids</h1>
  <p>Fun lessons, games, and an AI tutor for children aged 6–12. Learn math, reading, science and more.</p>
</div>
""", unsafe_allow_html=True)

# --- Subjects ---
st.markdown("## 📚 Explore Subjects")
st.divider()
st.markdown("## 💳 Plans & Pricing")
st.caption("Choose a monthly plan that works for your family.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🆓 Free")
    st.markdown("**$0 / month**")
    st.write("• Access to basic lessons")
    st.write("• Limited quizzes")
    st.write("• No AI tutor")
    st.button("Start Free", key="free_plan")

with col2:
    st.markdown("### ⭐ Basic")
    st.markdown("**$9 / month**")
    st.write("• All subjects unlocked")
    st.write("• Weekly quizzes")
    st.write("• AI tutor (limited)")
    st.button("Choose Basic", key="basic_plan")

with col3:
    st.markdown("### 🚀 Pro")
    st.markdown("**$19 / month**")
    st.write("• Unlimited lessons")
    st.write("• Daily quizzes & games")
    st.write("• AI tutor (unlimited)")
    st.button("Choose Pro", key="pro_plan")





c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown("<div class='card'>➕<br><b>Math</b></div>", unsafe_allow_html=True)
if "subject" not in st.session_state:
    st.session_state.subject = "Math"  # default
st.markdown("## 📚 Explore Subjects")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("➕ Math"):
        st.session_state.subject = "Math"

with c2:
    if st.button("📖 Reading"):
        st.session_state.subject = "Reading"

with c3:
    if st.button("🔬 Science"):
        st.session_state.subject = "Science"

with c4:
    if st.button("🎨 Art"):
        st.session_state.subject = "Art"

st.info(f"Currently learning: **{st.session_state.subject}**")

st.divider()

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

# --- Footer ---
st.markdown("---")
st.markdown("<center><small>© 2026 BrightKids • Built with ❤️ using AI</small></center>", unsafe_allow_html=True)


