import re
#import logging

from config import TOKEN, YANDEX_TRANSLATE_KEY
from telebot import TeleBot
import requests

#from db import Database


YANDEX_API = "https://translate.yandex.net/api/v1.5/tr.json/translate"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['t', 'translate'])
def translate(message):
    text = re.search(r"/t\s(.+)$", message.text).group(1)
    params = {
     "key": YANDEX_TRANSLATE_KEY,
     "text": text,
     "lang" : "ru-en"
    }
    response = requests.get(YANDEX_API, params=params)
    print("IN", message.text)
    print(response.content)
    response.raise_for_status()
    data = response.json()
    print("OUT", data['text'][0])
    bot.send_message(message.chat.id, data['text'][0])



@bot.message_handler(content_types=['text'])
def fallback(message):
    bot.send_message(
        message.chat.id, "Hi"
    )

if __name__ == "__main__":
    bot.polling(none_stop=True)