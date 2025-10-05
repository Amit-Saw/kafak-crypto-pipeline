# Kafka Crypto Pipeline

A real-time data pipeline that fetches cryptocurrency prices from CoinGecko API, processes them using Kafka Streams, and stores the results in MongoDB.

## Architecture

- **Producer**: Fetches live prices for Bitcoin and Ethereum every minute and sends to Kafka topic `api-raw-data`.
- **Kafka Streams**: Processes the raw data, adds enrichment (tag and timestamp), and forwards to `api-processed-data`.
- **Consumer**: Reads processed data and inserts into MongoDB collection `crypto_prices` in database `crypto_db`.

## Technologies Used

- Apache Kafka (with Zookeeper)
- Kafka Streams (Java)
- MongoDB
- Python (Producer and Consumer)
- Docker Compose

## Setup and Run

1. Start Docker containers:
   ```
   docker-compose up -d
   ```

2. Run Producer:
   ```
   cd producer
   python news_producer.py
   ```

3. Run Kafka Streams Processor:
   ```
   cd streams
   mvn clean compile exec:java -Dexec.mainClass="com.example.NewsStreamProcessor"
   ```

4. Run Consumer:
   ```
   cd consumer
   python mongo_consumer.py
   ```

5. Check data in MongoDB (using Compass or CLI).

## Data Flow

CoinGecko API → Producer → Kafka (api-raw-data) → Streams Processor → Kafka (api-processed-data) → Consumer → MongoDB
