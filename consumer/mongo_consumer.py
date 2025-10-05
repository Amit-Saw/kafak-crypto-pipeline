from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['crypto_db']
collection = db['crypto_prices']

# Kafka Consumer setup
consumer = KafkaConsumer(
    'api-processed-data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    crypto_data = message.value
    print(f"Inserting: {crypto_data['name']} - ${crypto_data['current_price']}")
    collection.insert_one(crypto_data)
