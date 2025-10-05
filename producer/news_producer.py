import requests
import json
import time
from kafka import KafkaProducer
from datetime import datetime

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# CoinGecko API for Bitcoin and Ethereum prices
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum"

while True:
    # Mock data for testing since API is blocked
    coins = [
        {
            'id': 'bitcoin',
            'name': 'Bitcoin',
            'current_price': 50000 + (time.time() % 1000),  # Mock price variation
            'market_cap': 1000000000000,
            'last_updated': datetime.now().isoformat()
        },
        {
            'id': 'ethereum',
            'name': 'Ethereum',
            'current_price': 3000 + (time.time() % 500),
            'market_cap': 300000000000,
            'last_updated': datetime.now().isoformat()
        }
    ]
    for coin in coins:
        record = {
            'id': coin['id'],
            'name': coin['name'],
            'current_price': coin['current_price'],
            'market_cap': coin['market_cap'],
            'last_updated': coin['last_updated'],
            'fetchedAt': datetime.now().isoformat()
        }
        producer.send('api-raw-data', value=record)
        print(f"Sent: {record['name']} - ${record['current_price']:.2f}")

    time.sleep(60)  # Fetch every minute
