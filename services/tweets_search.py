import datetime as dt

import tweepy

from services.services import fill_list_with_tweet_data, suitable_tweets_list


def global_search_tweets(api: tweepy.API, searching_phrases: tuple, time_from_which_start_search: dt.datetime
                         ) -> str | suitable_tweets_list:
    """Searching tweets by phrase throughout Twitter for the last 3 hours [en]
    Поиск твитов по фразе во всем Твиттере за последние 3 часа [ru]"""

    all_tweets_needed = []

    for phrase in searching_phrases:
        search_request = f"{phrase} -filter:replies -filter:retweets"
        tweets = api.search_tweets(q=search_request, tweet_mode="extended")
        tweets_list_from_json = [tweet for tweet in tweets if tweet.created_at > time_from_which_start_search]
        for tweet in tweets_list_from_json:
            fill_list_with_tweet_data(all_tweets_needed, tweet)
    if not all_tweets_needed:
        return "1 - Новых твитов за последние 3 часа не обнаружено 😪"
    return all_tweets_needed


def search_tweets_in_profiles(api: tweepy.API, searching_phrase: str, time_from_which_start_search: dt.datetime,
                              profiles: tuple) -> str | suitable_tweets_list:
    """Searching tweets by phrase in certain profiles for the last 3 hours [en]
    Поиск твитов по фразе в определенных профилях за последние 3 часа [ru]"""

    all_tweets_needed = []

    for profile in profiles:
        tweets = api.user_timeline(screen_name=profile, tweet_mode="extended")
        tweets_list_from_json = [tweet for tweet in tweets if tweet.created_at > time_from_which_start_search]
        for tweet in tweets_list_from_json:
            if all(word.lower() in tweet.full_text.lower() for word in searching_phrase.split()) and \
                    tweet.in_reply_to_status_id is None:
                fill_list_with_tweet_data(all_tweets_needed, tweet)
    if not all_tweets_needed:
        return "2 - Новых твитов за последние 3 часа не обнаружено 😪"
    return all_tweets_needed
