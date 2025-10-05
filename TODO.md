# TODO List for Kafka Crypto Pipeline

## 1. Update Producer (producer/news_producer.py)
- [x] Change API from NewsAPI to CoinGecko (free, no key required)
- [x] Fetch live prices for Bitcoin and Ethereum
- [x] Format data as JSON with fields: id, name, current_price, market_cap, last_updated, fetchedAt
- [x] Send to 'api-raw-data' topic

## 2. Fix Kafka Streams Processor (streams/src/main/java/com/example/NewsStreamProcessor.java)
- [x] Deserialize JSON value from String
- [x] Add enrichment: tag with "crypto" and add processedAt timestamp
- [x] Serialize back to JSON String
- [x] Output to 'api-processed-data' topic
- [x] Add Gson dependency to pom.xml

## 3. Fix Consumer (consumer/mongo_consumer.py)
- [x] Ensure it correctly inserts JSON data into MongoDB
- [x] Create consumer/requirements.txt with pymongo and kafka-python
- [x] Update to use crypto_db and crypto_prices collection, print name and price

## 4. Testing
- [x] Start Docker containers
- [x] Run producer, streams, consumer
- [x] Check MongoDB for inserted data
- [x] Upload to GitHub repository
