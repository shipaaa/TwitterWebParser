import datetime as dt

import tweepy

from services import fill_list_with_tweet_data


def global_search_tweets(api: tweepy.API, search_query: str, time_from_which_start_search: dt.datetime
                         ) -> str | list[dict[str, str]]:
    """Searching tweets by phrase throughout Twitter for the last 3 hours [en]
    Поиск твитов по фразе во всем Твиттере за последние 3 часа [ru]"""

    all_tweets_needed = []
    tweets = api.search_tweets(q=search_query, tweet_mode="extended")
    tweets_list_from_json = [tweet for tweet in tweets if tweet.created_at > time_from_which_start_search]
    if not tweets_list_from_json:
        return "Новых твитов за последние 3 часа не обнаружено 😪"
    for tweet in tweets_list_from_json:
        fill_list_with_tweet_data(all_tweets_needed, tweet)
    return all_tweets_needed


def search_tweets_in_profiles(api: tweepy.API, search_query: str, time_from_which_start_search: dt.datetime,
                              profiles: tuple) -> str | list[dict[str, str]]:
    """Searching tweets by phrase in certain profiles for the last 3 hours [en]
    Поиск твитов по фразе в определенных профилях за последние 3 часа [ru]"""

    all_tweets_needed = []

    for profile in profiles:
        query = f"{search_query} From:{profile}"
        tweets = api.search_tweets(q=query, tweet_mode="extended")
        if not tweets:
            continue
        tweets_list_from_json = [tweet for tweet in tweets if tweet.created_at > time_from_which_start_search]
        for tweet in tweets_list_from_json:
            fill_list_with_tweet_data(all_tweets_needed, tweet)
    if all_tweets_needed:
        return all_tweets_needed
    return "Новых твитов за последние 3 часа не обнаружено 😪"
