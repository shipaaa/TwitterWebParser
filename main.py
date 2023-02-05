import logging
import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger("tweepy")


def connect() -> tweepy.API:
    """Connecting to the Twitter API"""
    auth = tweepy.OAuth1UserHandler(
        consumer_key=os.environ.get('CONSUMER_KEY'), consumer_secret=os.environ.get('CONSUMER_SECRET'),
        access_token=os.environ.get('ACCESS_TOKEN'), access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
    )
    return tweepy.API(auth, proxy=os.getenv('PROXY'))


def search_tweets_by_word(keyword: str, from_datetime) -> None:
    """Searching tweets by word"""
    tweets = tweepy.Cursor(api.search_tweets, keyword, since_id=from_datetime).items(100)
    tweets_list = [_ for _ in tweets]
    for tweet in tweets_list:
        print(f'{tweet.created_at.strftime(f"%d-%m-%Y %H:%M:%S")} / {tweet.entities["urls"]}')
        # if len(tweet.entities["urls"]) == 0:
        #     continue
        # if tweet.entities["urls"][0]["expanded_url"][8:].split("/")[0] != "twitter.com":
        #     continue
        # print(f'{tweet.created_at.strftime(f"%d-%m-%Y %H:%M:%S")} / {tweet.entities["urls"][0]["expanded_url"]}')


if __name__ == "__main__":
    api = connect()
    search_words = "migration contract"
    new_search = search_words + " -filter:retweets" + " -filter:replies"
    from_date = "2023-01--28"

    search_tweets_by_word(new_search, from_date)
