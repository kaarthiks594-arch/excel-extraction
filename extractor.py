from docx import Document
import os
from doc_converter import convert_doc_to_docx

def extract_tables_from_doc(file):

    # Save uploaded file temporarily
    temp_path = file.name

    with open(temp_path, "wb") as f:
        f.write(file.getbuffer())

    # If file is .doc → convert
    if temp_path.lower().endswith(".doc") and not temp_path.lower().endswith(".docx"):
        temp_path = convert_doc_to_docx(os.path.abspath(temp_path))

    doc = Document(temp_path)
    extracted_data = []

    for table in doc.tables:
        for i, row in enumerate(table.rows):
            if i == 0:
                continue
            row_data = [cell.text.strip() for cell in row.cells]
            if any(cell != "" for cell in row_data):
                extracted_data.append(row_data)

    return extracted_data
