import streamlit as st
from pdf_parser import run_pdf_parser
from excel_parser import run_excel_parser

st.set_page_config(page_title="Bank Statement Toolkit", layout="wide")

st.sidebar.title("🔍 Select Mode")
mode = st.sidebar.radio("Choose a parser:", ["📄 PDF Bank Statement", "📊 Excel Bank Statement"])

if mode == "📄 PDF Bank Statement":
    run_pdf_parser()

elif mode == "📊 Excel Bank Statement":
    run_excel_parser()
