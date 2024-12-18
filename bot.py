import os
from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()
tg_api = os.getenv('TG_API')
bot = TeleBot(tg_api)


@bot.message_handler()
def send_some_message(message: types.Message):
    text = message.text
    bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.infinity_polling()
