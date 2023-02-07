import datetime as dt
import logging
import os
import time

import tweepy
from dotenv import load_dotenv

from search_tweets import global_search_tweets, search_tweets_in_profiles
from services import deduce_final_results

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

    last_few_hours_search_units = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc) - dt.timedelta(hours=3)
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

    phrase_for_global_search = "migration contract"
    global_search_request = f"{phrase_for_global_search} " \
                            f"-filter:replies -filter:retweets"
    phrase_for_certain_profiles = "new listing"

    tweets_by_phrase = global_search_tweets(connect_to_api, global_search_request, last_few_hours_search_units)
    tweets_in_certain_profiles = search_tweets_in_profiles(connect_to_api, phrase_for_certain_profiles,
                                                           last_few_hours_search_units, profile_references)

    deduce_final_results(tweets_by_phrase)
    deduce_final_results(tweets_in_certain_profiles)


if __name__ == "__main__":
    try:
        startTime = time.time()
        main()
        endTime = time.time()
        print(f"\n__main__ ends in {endTime - startTime} seconds...")
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
