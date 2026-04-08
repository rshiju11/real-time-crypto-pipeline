Author: Rshijuta Pokharel

------------PHASE 1------------

Real Time Crypto Data Pipeline

This project builds a real-time data pipeline that imgests live cryptocurrency prices, 
streams them through Kafka, and stores them in MySQL.

Tech Stack:
Python, Kafka, MySQL, Docker

Pipeline:
CoinGecko API -> Producer -> KAfka -> Consumer -> MySQL

Features:
- Fetches real-time crypto prices (Bitcoin, Ethereum)
- Streams data using Kafka
- Stores data in MySQL
- Handles API rate limiting

How to Run:

1 Start services
   docker compose up -d

2 Run consumner
    python3 app/consumer.py

3 Run producer
   python3 app/producer.py 

