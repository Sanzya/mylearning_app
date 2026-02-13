import streamlit as st

st.title("💳 Plans & Pricing")

plan = st.radio("Choose a plan:", ["Free ($0)", "Basic ($9/month)", "Pro ($19/month)"])

if st.button("Activate Plan"):
    st.session_state.plan = plan
    st.success(f"Plan activated: {plan}")

if "plan" in st.session_state:
    st.info(f"Current plan: {st.session_state.plan}")
