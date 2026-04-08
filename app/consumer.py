"""
consumer.py

- read messages from KAFKA
- parse JSON
- insert into MySQL
"""

import json
from kafka import KafkaConsumer
import mysql.connector

# KAFKA config
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "crypto_prices"

#MySQL config
DB_CONFIG = {"host": "localhost", "port": 3307, "user":"root", "password":"root", "database": "crypto_db"}

# connect to MySQL
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Create KAFKA consumer
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers= KAFKA_BROKER, value_deserializer=lambda x: json.loads(x.decode("utf-8")),
                         auto_offset_reset="earliest", enable_auto_commit=True)

print("Consumer started... Fetching form KAFKA")

# Read messages from Kafka
for message in consumer:
    data = message.value
    print("Received:", data)

    # Insert into MySQL
    insert_query = """
    INSERT INTO crypto_prices(
        coin_name, symbol, price_usd, change_24h, last_updated_at, fetched_at)
    VALUES (%s, %s, %s, %s,%s,%s)   

    """
    values=(data["coin_name"], data["symbol"], data["price_usd"], data["change_24h"], 
            data["last_updated_at"], data["fetched_at"])
    
    cursor.execute(insert_query, values)
    conn.commit()

    