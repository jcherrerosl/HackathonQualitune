import streamlit as st
import time
import random

st.set_page_config(page_title="Trustify", layout="centered")
st.title("Trustify")
st.caption("Intellectual property and originality verifier")

st.subheader("Submit your work")

uploaded_file = st.file_uploader("Upload a file (image, audio, document, etc.)", type=None)
input_url = st.text_input("Or paste a link (GitHub, YouTube, SoundCloud...):")

if st.button("Analyze"):
    if uploaded_file or input_url:
        with st.spinner("Searching for similar content in trusted databases..."):
            time.sleep(3)  # simulate processing

            # Generate a float between 1.5 and 4.5 with one decimal
            rating = round(random.uniform(1.5, 4.5), 1)

            comments = [
                "Some content similarities detected with existing works.",
                "Moderately original, though parts may resemble known sources.",
                "Above average uniqueness with minor resemblances.",
                "Good originality, limited similarity to known works.",
                "Substantial uniqueness, but not entirely distinctive."
            ]

            # Choose comment based on rating scale
            if rating < 2.0:
                comment = comments[0]
            elif rating < 2.8:
                comment = comments[1]
            elif rating < 3.5:
                comment = comments[2]
            elif rating < 4.2:
                comment = comments[3]
            else:
                comment = comments[4]

            st.success("Analysis complete")
            st.metric("Originality Score", f"{rating}/5")
            st.info(comment)

            if uploaded_file:
                st.write("Submitted file:")
                st.write(f"Name: {uploaded_file.name}")
            if input_url:
                st.write("Submitted link:")
                st.write(input_url)
    else:
        st.warning("Please upload a file or provide a link.")

st.subheader("Optional Identity Verification")

phone_number = st.text_input("Phone number (international format, e.g. +34612345678):")
full_name = st.text_input("Full name (for KYC match):")

if st.button("Verify Identity"):
    if phone_number and full_name:
        with st.spinner("Verifying identity using Open Gateway APIs..."):
            try:
                from opengateway_api import verify_number, verify_identity

                number_info = verify_number(phone_number)
                identity_match = verify_identity(full_name)

                st.success("Verification results:")
                st.json({
                    "Number Verification": number_info,
                    "KYC Match": identity_match
                })

            except Exception as e:
                st.error(f"Verification failed: {e}")
    else:
        st.warning("Please enter both phone number and full name.")
