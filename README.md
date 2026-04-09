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
- Real-time crypto data ingestion using Kafka
- Data storage in MySQL (Dockerized)
- Interactive dashboard using Streamlit
- Live price visualization

How to Run:

```bash
docker-compose up -d
python app/producer.py
python app/consumer.py
streamlit run dashboard/dashboard.py

