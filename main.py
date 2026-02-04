# =============================
# Gemini Search Engine UI (Python)
# =============================
# This app creates a simple web-based search engine UI using Streamlit
# and calls Google's Gemini API to get responses.

# --------- REQUIREMENTS ---------
# 1. Python 3.9+
# 2. Install dependencies:
#    pip install streamlit google-generativeai
# 3. Get your Gemini API key from Google AI Studio

# --------- HOW TO RUN ---------
# streamlit run app.py

# --------- FILE NAME ---------
# Save this as: app.py

import streamlit as st
import google.generativeai as genai

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Gemini Search Engine", layout="centered")
st.title("🔍 Gemini Search Engine")
st.write("Ask anything and get answers from Gemini AI.")

# ---------------- API KEY ----------------
# Option 1 (Recommended): Set environment variable
# export GOOGLE_API_KEY="your_api_key_here"

# Option 2: Paste directly (not secure for production)
API_KEY = "AIzaSyD-gze8XMtxarXUsKGSu4yGx34Ejpzf0CE"

if API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    st.warning("⚠️ Please add your Gemini API key in the code.")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")



# ---------------- UI ----------------
query = st.text_input("Enter your search query:")

if st.button("Search") and query:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(query)
            st.subheader("📌 Gemini Response")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ using Python, Streamlit & Gemini API")
