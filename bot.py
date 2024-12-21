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


@bot.message_handler(content_types=["sticker"])
def handle_sticker(message: types.Message):
    bot.send_sticker(
        chat_id=message.chat.id,
        sticker=message.sticker.file_id,
        reply_to_message_id=message.id,
    )


def is_cat_in_caption(message: types.Message):
    return message.caption and "кот" in message.caption.lower()


@bot.message_handler(content_types=["photo"], func=is_cat_in_caption)
def handle_caption_photo(message: types.Message):    
    bot.send_message(
        chat_id=message.chat.id,
        text="Котики это хорошо!)",
        reply_to_message_id=message.id
    )
    photo_file_id = content.PICS_DOGS
    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_file_id,
        caption="Я люблю собачек)"
    )


@bot.message_handler(content_types=["photo"])
def handle_foto(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="👍",
        reply_to_message_id=message.id
    )


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
