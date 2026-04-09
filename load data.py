import pandas as pd
import os
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="stock_analysis"
)
cursor = conn.cursor()            # The cursor is used to run SQL commands and fetch results

folder = r"C:\Users\Dell\Desktop\Stock market\DataSets"

rename_map = {
    "Date": "trade_date",
    "Symbol": "stock_symbol",
    "Open": "open_price",
    "High": "high_price",
    "Low": "low_price",
    "Close": "close_price",
    "Volume": "volume"
}

insert_sql = """
INSERT INTO stock_prices
(trade_date, stock_symbol, open_price, high_price, low_price, close_price, volume)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for file in os.listdir(folder):
    if file.endswith(".csv") and file != "stock_metadata.csv" and file != "NIFTY50_all.csv":
        df = pd.read_csv(os.path.join(folder, file))

        df = df[list(rename_map.keys())]
        df = df.rename(columns=rename_map)

        df["trade_date"] = pd.to_datetime(df["trade_date"], errors="coerce")
        df.dropna(subset=["trade_date"], inplace=True)   # Delete rows where date is missing or invalid & Which columns matter for dropping rows
 
        for _, row in df.iterrows():             # iterate over each row and ignore index
            cursor.execute(insert_sql, tuple(row))   # fill the placeholders and send to database

        conn.commit()        # Save changes and Permanently writes data to the database
        print(f"Loaded {file}")

cursor.close()
conn.close()
