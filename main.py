import streamlit as st
from pdf_parser import run_pdf_parser
from excel_parser import run_excel_parser

# === FIRST: set page config ===
st.set_page_config(page_title="Bank Statement Toolkit", layout="wide")

# === PASSWORD PROTECTION ===
def authenticate():
    st.title("🔒 Secure Access")

    password = st.text_input("Enter password to access the app:", type="password")
    if password == "nfsu@@23":  # 🔐 Replace with your actual password
        st.success("🔓 Access granted!")
        return True
    elif password:
        st.error("❌ Incorrect password. Please try again.")
        return False
    return False

if authenticate():
    st.sidebar.title("🔍 Select Mode")
    mode = st.sidebar.radio("Choose a parser:", ["📄 PDF Bank Statement", "📊 Excel Bank Statement"])

    if mode == "📄 PDF Bank Statement":
        run_pdf_parser()
    elif mode == "📊 Excel Bank Statement":
        run_excel_parser()
