import datetime as dt

import tweepy


def global_search_tweets(api: tweepy.API, search_query: str, time_from_which_start_search: dt.datetime) -> str | list:
    """Searching tweets by phrase throughout Twitter for the last 3 hours [en]
    Поиск твитов по фразе во всем Твиттере за последние 3 часа [ru]"""

    all_tweets_list = []
    tweets = api.search_tweets(q=search_query, tweet_mode="extended")
    tweets_list_from_json = [tweet for tweet in tweets if tweet.created_at > time_from_which_start_search]
    if not tweets_list_from_json:
        return "Никаких новых твитов за последние 3 часа не обнаружено 😪"
    for tweet in tweets_list_from_json:
        all_tweets_list.append({
            "tweet_created_at": tweet.created_at.replace(tzinfo=dt.timezone.utc).astimezone(tz=None).strftime(
                f"%d-%m-%Y %H:%M:%S"),
            "tweet_url": f"https://twitter.com/{tweet.author.screen_name}/status/{tweet.id}",
            "tweet_text": tweet.full_text})
    return all_tweets_list


def search_tweets_in_profiles(api: tweepy.API, search_query: str, time_from_which_start_search: dt.datetime,
                              profiles: tuple) -> None:
    """Searching tweets by phrase in certain profiles for the last 3 hours [en]
    Поиск твитов по фразе в определенных профилях за последние 3 часа [ru]"""
