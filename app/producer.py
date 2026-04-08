import json
import time
from datetime import datetime, timezone

import requests
from kafka import KafkaProducer

# kafka settings
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "crypto_prices"

# Endpoint: CoinGecko API
API_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum"
    "&vs_currencies=usd"
    "&include_24hr_change=true"
    "&include_last_updated_at=true"
)

# kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# call CoinGecko API and get live data
def fetch_prices():
    response = requests.get(API_URL,timeout=10)
    response.raise_for_status()
    return response.json()

# take raw JSON file and convert it to cleaner str for KAfka
def build_events(data):
    events=[]
    fetched_at = datetime.now(timezone.utc).isoformat()

    for coin_name, values in data.items():
        
        event = { "coin_name": coin_name, "symbol": coin_name[:3].upper(), "price_usd": values.get("usd"),
        "change_24h": values.get("usd_24h_change"), "last_updated_at": values.get("last_updated_at"),
        "fetched_at": fetched_at}
    
        events.append(event)
    return events

# fetches data every 10 secs
def main():
    while True:
        try:
            data= fetch_prices()
            events = build_events(data)

            for event in events:
                producer.send(TOPIC_NAME, value=event)
                print("sent to Kafka:", event)
            
            producer.flush()
            time.sleep(20)

        except Exception as e:
            print("Error:", e)
            print("Cooling down... waiting 120 seconds")

            time.sleep(120)

if __name__ == "__main__":
    main()



