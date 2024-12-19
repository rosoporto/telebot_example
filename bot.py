import os
import random
import content
from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()
tg_api = os.getenv('TG_API')
bot = TeleBot(tg_api)


@bot.message_handler(commands=["start"])
def handler_command_start(message: types.Message):
    bot.send_message(message.chat.id, "Пртвет!)")


@bot.message_handler(commands=["help"])
def handler_command_start(message: types.Message):
    bot.send_message(message.chat.id, content.help)


@bot.message_handler(commands=["joke"])
def handler_command_start(message: types.Message):
    joke = random.choice(content.jokes)
    bot.send_message(message.chat.id, joke)


@bot.message_handler()
def send_hello_message(message: types.Message):
    text = message.text
    text_lower = text.lower()
    if "привет" in text_lower:
        text = "И тебе привет!"
    elif "как дела" in text_lower:
        text = "Хорошо! А у вас как?"
    elif "пока" in text_lower or "до свидания" in text_lower:
        text = "До новых встреч!"
    bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
