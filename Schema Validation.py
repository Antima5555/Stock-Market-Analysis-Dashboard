# We validated only the necessary fact-table columns instead of the full schema, so the 
# ETL runs faster and scales better.


expected_cols = {
    "Date", "Symbol", "Open", "High", "Low", "Close", "Volume"
}


import pandas as pd
import os

folder = r"C:\Users\Dell\Desktop\Stock market\DataSets"
invalid_files = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file), nrows=1)
        cols = set(df.columns)

        if not expected_cols.issubset(cols):
            invalid_files.append(file)

print("Invalid files:", invalid_files)

