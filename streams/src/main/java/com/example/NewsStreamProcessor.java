// RUNNING THE STREAMS APPLICATION
// cd streams
//mvn clean compile exec:java -Dexec.mainClass="com.example.NewsStreamProcessor"


package com.example;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonPrimitive;
import com.google.gson.Gson;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.StreamsConfig;

import java.util.Properties;
import java.time.Instant;

public class NewsStreamProcessor {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "news-streams-app");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> source = builder.stream("api-raw-data");

        Gson gson = new Gson();

        KStream<String, String> transformed = source.mapValues(value -> {
            // Parse JSON string to JsonObject
            JsonObject json = JsonParser.parseString(value).getAsJsonObject();

            // Add tag "crypto"
            json.add("tag", new JsonPrimitive("crypto"));

            // Add processedAt timestamp
            json.add("processedAt", new JsonPrimitive(Instant.now().toString()));

            // Convert back to JSON string
            return gson.toJson(json);
        });

        transformed.to("api-processed-data");

        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
