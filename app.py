import streamlit as st
import pandas as pd
import random
import time
from opengateway_api import verify_number

st.set_page_config(page_title="Trustify", layout="centered")
st.title("Trustify")
st.caption("AI-based trust & originality filter for digital content")

# ---- Identity Verification via SMS ----
st.subheader("Identity Verification (Required)")

if 'verification_passed' not in st.session_state:
    st.session_state.verification_passed = False

phone_number = st.text_input("📱 Phone number (e.g. +34612345678):")

if st.button("Verify via SMS"):
    if phone_number:
        with st.spinner("Sending verification request via SMS..."):
            time.sleep(7)  # simulate network delay
            try:
                result = verify_number(phone_number)
                st.success("✅ Number Verified")
                st.json(result)
                st.session_state.verification_passed = True
            except Exception as e:
                st.error(f"❌ Verification failed: {e}")
                st.session_state.verification_passed = False
    else:
        st.warning("Please enter a phone number to continue.")

# ---- Content Submission ----
if st.session_state.verification_passed:
    st.subheader("Submit Content for Trust Check")

    url_input = st.text_input("Paste a URL (YouTube, SoundCloud, GitHub, etc.):")
    uploaded_file = st.file_uploader("Or upload a file (image, audio, etc.):", type=["mp3", "wav", "png", "jpg", "pdf", "zip"])

    if st.button("Run Trustify Check"):
        if not url_input and not uploaded_file:
            st.warning("Please upload a file or paste a URL.")
        else:
            with st.spinner("Analyzing for originality and trust..."):
                time.sleep(3)  # simulate processing time
                score = round(random.uniform(1.2, 2.1), 1)  # evitar extremos 0 y 5
                verdict = ""

                if score < 2.0:
                    verdict = "⚠️ High risk of plagiarism or duplication."
                elif score < 3.5:
                    verdict = "⚠️ Partial similarity to known content."
                else:
                    verdict = "✅ High originality detected."

                st.subheader("Results")
                st.metric(label="Originality Score (0–5)", value=score)
                st.write(verdict)

                if uploaded_file:
                    st.info(f"File submitted: `{uploaded_file.name}`")
                if url_input:
                    st.info(f"URL submitted: {url_input}")
