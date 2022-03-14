from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob

es = Elasticsearch(hosts=['localhost'],port=9200)

def main():
    '''
    main function initiates a kafka consumer, initialize the tweetdata database.
    Consumer consumes tweets from producer, extracts features, cleanses the tweet text,
    calculates sentiments and loads the data into elasticsearch
    '''

    # ask for specific hashtag
    hashtag = input("Enter the hashtag (do not include '#') : ")

    # set-up a Kafka consumer
    consumer = KafkaConsumer("twitter"+hashtag)
    for msg in consumer:

        dict_data = json.loads(msg.value)
        tweet = TextBlob(dict_data["text"])
        
        #sentiment analysis using TextBlob's .sentiment.polarity
        #it returns a value within the range of -1 to 1 being negative to positive
        tw_sentiment = ''

        if tweet.sentiment.polarity > 0:
            tw_sentiment = 'positive'
        elif tweet.sentiment.polarity < 0:
            tw_sentiment = 'negative'
        elif tweet.sentiment.polarity == 0:
            tw_sentiment = 'neutral'
        
        # add text and sentiment info to elasticsearch
        es.index(index="tweet" + hashtag,
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "sentiment": tw_sentiment})

        print(tweet)
        print('\n')

if __name__ == "__main__":
    main()