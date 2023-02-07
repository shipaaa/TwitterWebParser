import datetime as dt


def deduce_final_results(function_result: str | list[dict[str, str]], parser_number: int) -> None:
    """Function for output of results [en]
    Функция для вывода результатов [ru]"""

    print(f"{10 * '-'}Парсер №{parser_number}{10 * '-'}\n")

    if not isinstance(function_result, str):
        for tweet in function_result:
            print(f"{tweet['tweet_created_at']}\n{tweet['tweet_url']}\n{tweet['tweet_text']}\n")
    else:
        print(function_result)


def fill_list_with_tweet_data(data_list: list[dict[str, str]], tweet_data) -> list:
    """Select from the data that comes in the form of a json file that we need and add them to the list [en]
    Выбираем из данных, которые приходят в виде json файла, необходимые нам и добавляем их в список [ru]"""
    data_list.append({
        "tweet_created_at": tweet_data.created_at.replace(tzinfo=dt.timezone.utc).astimezone(tz=None).strftime(
            "%d-%m-%Y %H:%M:%S"),
        "tweet_url": f"https://twitter.com/{tweet_data.author.screen_name}/status/{tweet_data.id}",
        "tweet_text": tweet_data.full_text
    })
    return data_list
