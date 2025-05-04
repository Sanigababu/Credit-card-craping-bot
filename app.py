import streamlit as st
from url_scraper import parse_url
from pdf_scraper import parse_pdf
from exporter import export_to_json, export_to_excel
import os
import json
import pandas as pd

st.set_page_config(page_title="Credit Card Scraper", layout="centered")
st.title("💳 Credit Card Scraper")

# Input section
st.subheader("Input Source")
input_type = st.radio("Choose input type:", ["URL", "PDF File"])

cards = []

if input_type == "URL":
    url = st.text_input("Enter the URL:")
    if url and st.button("Scrape URL"):
        with st.spinner("Scraping URL..."):
            cards = parse_url(url)

elif input_type == "PDF File":
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file and st.button("Scrape PDF"):
        with st.spinner("Scraping PDF..."):
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())
            cards = parse_pdf("temp.pdf")
            os.remove("temp.pdf")

# Display results
if cards:
    st.success(f"Found {len(cards)} credit card(s).")
    for card in cards:
        st.markdown("---")
        st.write(f"**{card.get('name', 'Unnamed Card')}**")
        for k, v in card.items():
            if k != "name":
                st.write(f"- **{k}**: {v}")

    # Export options
    st.subheader("Export Results")

    export_format = st.radio("Select output format:", ["JSON"])
    if export_format == "JSON":
        export_to_json(cards, "output.json")
        with open("output.json", "rb") as f:
            st.download_button("📥 Download JSON", f, file_name="credit_cards.json")

    
