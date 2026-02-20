from docx import Document

EXPECTED_KEYWORDS = [
    "Type",
    "Ref",
    "Hazardous",
    "Cause",
    "Effect",
    "Protective",
    "Residual"
]

def is_valid_risk_table(table):
    header_text = " ".join([cell.text.strip() for cell in table.rows[0].cells])

    match_count = sum(1 for word in EXPECTED_KEYWORDS if word.lower() in header_text.lower())

    return match_count >= 4   # minimum match condition


def extract_tables_from_doc(file):
    doc = Document(file)
    extracted_data = []

    for table in doc.tables:
        if is_valid_risk_table(table):
            for i, row in enumerate(table.rows):
                if i == 0:
                    continue  # skip header

                row_data = [cell.text.strip() for cell in row.cells]
                extracted_data.append(row_data)

    return extracted_data
