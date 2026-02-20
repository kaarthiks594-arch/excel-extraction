import streamlit as st
import pandas as pd
from extractor import extract_tables_from_doc
from formatter import convert_to_dataframe

st.title("ISO 14798 Risk Assessment Extractor")

uploaded_files = st.file_uploader(
    "Upload Risk Assessment DOCX Files",
    type=["docx"],
    accept_multiple_files=True
)

if uploaded_files:
    all_data = []

    for file in uploaded_files:
        data = extract_tables_from_doc(file)
        all_data.extend(data)

    if all_data:
        df = convert_to_dataframe(all_data)

        st.success("Extraction Completed!")
        st.dataframe(df)

        df.to_excel("output/Combined_Risk_Assessment.xlsx", index=False)

        with open("output/Combined_Risk_Assessment.xlsx", "rb") as f:
            st.download_button(
                "Download Excel File",
                f,
                file_name="Combined_Risk_Assessment.xlsx"
            )
    else:
        st.warning("No matching Risk Assessment tables found.")
