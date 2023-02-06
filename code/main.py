import datetime as dt
import logging
import os
import time

import tweepy
from dotenv import load_dotenv

from search_tweets import global_search_tweets, search_tweets_in_profiles

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger("__name__")


def main():
    load_dotenv()
    authentication = tweepy.OAuth1UserHandler(
        consumer_key=os.environ.get('CONSUMER_KEY'), consumer_secret=os.environ.get('CONSUMER_SECRET'),
        access_token=os.environ.get('ACCESS_TOKEN'), access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
    )
    connect_to_api = tweepy.API(authentication, proxy=os.getenv('PROXY'))

    phrase = "migration contract"
    search_request = f"{phrase} -filter:replies -filter:retweets " \
                     f"since:{(dt.datetime.utcnow() - dt.timedelta(days=1)).strftime('%Y-%m-%d')}"
    last_few_hours_search_units = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc) - dt.timedelta(hours=3)

    tweets_by_phrase = global_search_tweets(connect_to_api, search_request, last_few_hours_search_units)
    if isinstance(tweets_by_phrase, str):
        result = tweets_by_phrase
        print(result)
    else:
        for tweet in tweets_by_phrase:
            print(f"{tweet['tweet_created_at']}\n{tweet['tweet_url']}\n{tweet['tweet_text']}\n")

    # Начало 2 парсера
    profile_references = (
        "LBank_Exchange",
        "ZT_Exchange",
        "BitrueOfficial",
        "Hotbit_news",
        "XTexchange",
        "bitgetglobal",
        "Bibox365",
        "_AscendEX",
    )
    search_tweets_in_profiles(connect_to_api, "tag", last_few_hours_search_units, profile_references)


if __name__ == "__main__":
    try:
        startTime = time.time()
        main()
        endTime = time.time()
        print(f'Program was finished in {endTime - startTime} seconds...')
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
