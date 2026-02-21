import streamlit as st
import pandas as pd
from extractor import extract_tables_from_doc
from formatter import convert_to_dataframe
from io import BytesIO

st.set_page_config(page_title="ISO Risk Extractor", layout="wide")

st.title("ISO 14798 Risk Assessment Extractor")
st.write("Upload multiple DOCX files to extract ISO 14798 Risk Tables.")

uploaded_files = st.file_uploader(
    "Upload Risk Assessment DOCX Files",
    type=["docx"],
    accept_multiple_files=True
)

if uploaded_files:
    all_data = []
    progress_bar = st.progress(0)

    for i, file in enumerate(uploaded_files):
        data = extract_tables_from_doc(file)
        all_data.extend(data)
        progress_bar.progress((i + 1) / len(uploaded_files))

    if all_data:
        df = convert_to_dataframe(all_data)

        st.success(f"Extraction Completed! {len(df)} rows extracted.")
        st.dataframe(df, use_container_width=True)

        # Convert to Excel in memory
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        st.download_button(
            label="Download Combined Excel File",
            data=output,
            file_name="Combined_Risk_Assessment.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    else:
        st.warning("No matching ISO 14798 Risk tables found.")
