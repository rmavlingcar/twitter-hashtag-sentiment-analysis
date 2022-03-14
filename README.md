# Twitter Hashtag Sentiment Analysis
Implementing a framework to perform sentiment analysis of a given hashtag in realtime using Apache Kafka, TextBlob, Twitter API, Elasticsearch and Kibana.

## 1) Scrapper
The scrapper collects all tweets, preprocessing them before it is sent to Kafka for analytics.
The scrapper is a standalone program and performs the following:

- Collects tweets in real-time with particular hash tags. 

- After filtering, it send them to Kafka using Kafka API
https://kafka.apache.org/090/documentation.html\#producerapi

- The scrapper program runs infinitely and take hash tags as input parameter while running.

## 2) Kafka

Kafka needs to be installed and run with Zookeeper. We create a dedicated topic for data transport.

## 3) Spark Streaming

In Spark Streaming, we create a Kafka consumer that periodically collect
filtered tweets from scrapper. For each hash tag, perform sentiment
analysis using Sentiment Analyzing tool.

## 4) Sentiment Analysis

Sentiment Analysis is the process of determining whether a piece of
writing is positive, negative, or neutral.

Sentiment analysis on tweets is done using TextBlob's 'sentiment.polarity' feature to attribute a positive or negative sentiment and adds that information to elasticsearch.

## 5) Elasticsearch and Kibana

Elasticsearch is used to store the tweets along with their sentiment analysis results for further visualisation purposes.

Kibana is a visualisation tool that we use to explore the data we have gathered in elasticsearch. The visualisation tool can be used to view the results of our sentiment classification in real-time.
