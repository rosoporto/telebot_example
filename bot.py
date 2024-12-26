import os
import random
import content
import my_filter
from dotenv import load_dotenv
from io import StringIO
from telebot import TeleBot, types, custom_filters, formatting
from get_joke_frop_api import get_joke_single, get_joke_twopart


load_dotenv()
tg_api = os.getenv('TG_API')
bot = TeleBot(tg_api)
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.ForwardFilter())
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(my_filter.IsUserBotAdmin())
bot.add_custom_filter(my_filter.ContainsWordFilter())


@bot.message_handler(commands=["start"])
def handler_command_start(message: types.Message):
    bot.send_message(message.chat.id, "Пртвет!)")


@bot.message_handler(commands=["help"])
def handler_command_start(message: types.Message):
    bot.send_message(message.chat.id, content.help)


@bot.message_handler(commands=["joke"])
def handler_command_start(message: types.Message):
    # joke = random.choice(content.jokes)
    joke = get_joke_single()
    joke = formatting.hcite(joke)
    bot.send_message(
        message.chat.id,
        joke,
        parse_mode="HTML")


@bot.message_handler(commands=["joke2"])
def handler_command_start(message: types.Message):    
    setup, delivery = get_joke_twopart()
    joke = formatting.format_text(
        formatting.escape_html(setup),
        formatting.hspoiler(delivery),
    )
    bot.send_message(
        message.chat.id,
        joke,
        parse_mode="HTML")


# add custom filter created by me
@bot.message_handler(commands=["secret"], is_user_bot_admin=True)
def handler_secret_request(message: types.Message):    
    bot.send_message(
        message.chat.id,
        text="Секрет для админа"
    )


@bot.message_handler(commands=["secret"], is_user_bot_admin=False)
def handler_secret_request_not_admin(message: types.Message):    
    bot.send_message(
        message.chat.id,
        text="Доступ закрыт"
    )


@bot.message_handler(commands=["chat_id"])
def handler_chat_id_request(message: types.Message):    
    bot.send_message(
        message.chat.id,
        text=f"Id чата: {message.chat.id}"
    )


@bot.message_handler(is_reply=True)
def echo_message_reply(message: types.Message):
    message_type = message.reply_to_message.content_type
    content_type_to_ru = content.content_type_to_ru
    
    if message_type in content_type_to_ru:
        message_type = content_type_to_ru[message_type]
    
    # processing messages from other places is mandatory *.escape_*
    text = (
        "Вы <b>ответили</b> на сообщение, "
        rf"Тип - {formatting.escape_html(message_type)}."
    )
    bot.send_message(
        message.chat.id,
        text=text,
        reply_to_message_id=message.reply_to_message.id,
        parse_mode="HTML", # or MarkdownV2
    )


@bot.message_handler(commands=["set_photo"])
def set_photo_from_disk(message: types.Message):
    photo_file = types.InputFile("pics/cat.jpg")
    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_file,
        caption="Картинка с диска"
    )


@bot.message_handler(commands=["set_photo_doc"])
def set_photo_from_disk_as_doc(message: types.Message):
    photo_file = types.InputFile("pics/cat.jpg")
    bot.send_document(
        chat_id=message.chat.id,
        document=photo_file,
        caption="Картинка как документ"
    )


@bot.message_handler(commands=["set_photo_doc_id"])
def set_photo_from_disk_as_doc_id(message: types.Message):
    photo_file_id = content.PICS_CAT_ID
    bot.send_document(
        chat_id=message.chat.id,
        document=photo_file_id,
        caption="Картинка как документ по ссылке"
    )


@bot.message_handler(commands=["set_photo_id"])
def set_photo_id(message: types.Message):
    photo_file = types.InputFile("pics/cat.jpg")
    bot.send_photo(
        chat_id=message.chat.id,
        photo=content.PICS_CAT_ID,
        caption="Картинка по ID"
    )


@bot.message_handler(content_types=["sticker"])
def handle_sticker(message: types.Message):
    bot.send_sticker(
        chat_id=message.chat.id,
        sticker=message.sticker.file_id,
        reply_to_message_id=message.id,
    )

# example using func for filter
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


# example using custom filter
@bot.message_handler(content_types=["photo"], contains_word="собака")
def handle_caption_photo(message: types.Message):    
    bot.send_message(
        chat_id=message.chat.id,
        text="О, мы про собачек?..",
        reply_to_message_id=message.id
    )
    photo_file_id = content.PICS_DOGS
    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_file_id,
        caption="Мне эти нравятся)"
    )


@bot.message_handler(content_types=["photo"])
def handle_foto(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="👍",
        reply_to_message_id=message.id
    )


@bot.message_handler(commands=["file"])
def set_file(message: types.Message):
    file_doc = types.InputFile("contents/text.txt")
    bot.send_document(
        chat_id=message.chat.id,
        document=file_doc,
        caption="Вот ваш файл с текстом"
    )


@bot.message_handler(commands=["file_gen"])
def set_file_from_memory(message: types.Message):
    file = StringIO()
    file.write("Привет!\n")
    file.write("Это сгенерированный файл с текстом на лету!\n")
    file.seek(0) #переведи каретку в начало документа
    file_from_memory = types.InputFile(file)
    bot.send_document(
        chat_id=message.chat.id,
        document=file_from_memory,
        caption="Сгенерированный файл с текстом на лету",
        visible_file_name="file_gen.txt"
    )


@bot.message_handler(commands=["text"], is_forwarded=True)
def message_handle_forward_check(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=content.DONT_FORWARD_CONTENT,
    )

@bot.message_handler(text=custom_filters.TextFilter(
    contains=["погода"],
    ignore_case=True,
))
def heandle_weather_request(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=formatting.mbold("Хорошая"),
        parse_mode="MarkdownV2"
    )


@bot.message_handler(commands=["md"])
def set_markdownV2(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=content.MarkdownV2,
        parse_mode="MarkdownV2"
    )


@bot.message_handler(commands=["html"])
def set_markdownV2(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=content.html,
        parse_mode="HTML"
    )


# copying message as is (italic, bold, ...)
@bot.message_handler(contains_word="проверка")
def copy_incoming_gmessage(message: types.Message):
    if message.entities:
        for entity in message.entities:
            print(entity)
    bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.id
    )


@bot.message_handler()
def send_echo_message(message: types.Message):
    text = message.text    
    bot.send_message(
        message.chat.id,
        text,
        entities=message.entities
    )


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
