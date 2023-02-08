import datetime as dt
import os

import requests
from dotenv import load_dotenv


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


def deduce_final_results(function_result: str | list[dict[str, str]], parser_number: int) -> None:
    """Function for output of results [en]
    Функция для вывода результатов [ru]"""
    if not isinstance(function_result, str):
        for tweet in function_result:
            send_results_to_telegram(f"{tweet['tweet_created_at']}\n{tweet['tweet_url']}\n{tweet['tweet_text']}\n",
                                     parser_number)
    else:
        send_results_to_telegram(function_result, parser_number)


def send_results_to_telegram(text_message: str, parser_number: int):
    """Sending data to telegram using a POST request to the Telegram API and the requests library [en]
    Отправка данных в телеграм с помощью POST запроса к API Telegram и библиотеки requests [ru]"""
    load_dotenv()
    url = f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_BOT_TOKEN')}/sendMessage"
    if parser_number == 1:
        requests.post(url, data={
            "chat_id": os.environ.get('TELEGRAM_CHAT_ID_1'),
            "text": text_message
        })
    elif parser_number == 2:
        requests.post(url, data={
            "chat_id": os.environ.get('TELEGRAM_CHAT_ID_1'),
            "text": text_message
        })
