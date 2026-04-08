"""
test_db.py

to check if python is reading data from my database
"""

import pandas as pd
import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(host="localhost", port=3307, user="root", password="root", database="crypto_db")

query = """
SELECT symbol, price_usd
FROM crypto_prices
ORDER BY fetched_at DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

conn.close()
print(df)