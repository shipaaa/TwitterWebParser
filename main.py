import datetime as dt
import logging
import os
import time

import tweepy
from dotenv import load_dotenv

from services.tweets_search import global_search_tweets, search_tweets_in_profiles
from services.services import deduce_final_results

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger("__name__")


def main():
    # Connecting to the Twitter API [en] | Соединение с API Твиттера [ru]
    load_dotenv()
    authentication = tweepy.OAuth1UserHandler(
        consumer_key=os.environ.get('CONSUMER_KEY'), consumer_secret=os.environ.get('CONSUMER_SECRET'),
        access_token=os.environ.get('ACCESS_TOKEN'), access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
    )
    connect_to_api = tweepy.API(authentication, proxy=os.getenv('PROXY'))

    last_few_hours_search_units = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc) - dt.timedelta(hours=3)
    """The time from which we want to find the tweets. In this example, the search takes place in the last 3 hours [en]
    Время с момента которого мы хотим найти твиты. В данном примере Поиск происходит за последние 3 часа [ru]"""

    profile_references: tuple = ("dog_rates",)
    """User profiles for which you need to search by the 2nd method. Passed to the variable in the form: (your 
    profile: https://twitter.com/dog_rates, the way to write this to the list of profiles: dog_rates) [en] Профили 
    пользователей по которым нужно осуществить поиск 2м методом. Передается переменной в виде: (ваш профиль: 
    https://twitter.com/dog_rates, записывается в список профилей: dog_rates) [ru]"""

    phrases_for_global_search: tuple = ("cat",)
    """Phrases that we want to find by the 1st method (global search) [en]
    Словосочетания, которые мы хотим найти 1м методом (глобальный поиск) [ru]"""

    phrase_for_certain_profiles_search: str = "new listing"
    """The phrase we want to find by the 2nd method (search by specific profiles)
    Словосочетание, которую мы хотим найти 2м методом (поиск по конкретным профилям)"""

    tweets_in_global_search = global_search_tweets(connect_to_api, phrases_for_global_search,
                                                   last_few_hours_search_units)
    tweets_in_certain_profiles = search_tweets_in_profiles(connect_to_api, phrase_for_certain_profiles_search,
                                                           last_few_hours_search_units, profile_references)

    deduce_final_results(tweets_in_global_search, 1)
    deduce_final_results(tweets_in_certain_profiles, 2)


if __name__ == "__main__":
    try:
        while True:
            main()
            time.sleep(60 * 60 * 3)
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
