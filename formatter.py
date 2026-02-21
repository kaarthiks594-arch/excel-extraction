import pandas as pd

FINAL_COLUMNS = [
    "Type",
    "Ref. No / Deviation",
    "Hazardous Situation",
    "Cause",
    "Effect",
    "S",
    "P",
    "Protective measures (risk reduction measure)",
    "After protective measures S",
    "After protective measures P",
    "Residual Risk"
]

def convert_to_dataframe(all_data):
    df = pd.DataFrame(all_data)

    # Adjust column size safely
    if df.shape[1] < len(FINAL_COLUMNS):
        for i in range(len(FINAL_COLUMNS) - df.shape[1]):
            df[df.shape[1]] = ""

    df = df.iloc[:, :len(FINAL_COLUMNS)]
    df.columns = FINAL_COLUMNS

    return df
