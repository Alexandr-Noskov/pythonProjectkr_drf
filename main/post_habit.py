import os
import requests

from dotenv import load_dotenv

load_dotenv

TOKEN = os.getenv('TOKEN_PASS')


def handle(message):    # функция отправки собщения в чат
    chat_id = "476890564"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()  # Эта строка отсылает сообщение