help = """Привет! Доступные команды:
/start - Старт бота
/help - Помощь (это сообщение)
/joke - Шутка дня)
"""

jokes = [
    "Почему программисты не любят природу? Потому что в ней слишком много багов!",
    "Какой самый оптимистичный овощ? Морковь, потому что она всегда находит свой корень!",
    "Почему книга по математике была грустной? У нее было слишком много проблем!",
    "Какой любимый напиток у вампиров? Кровавая Мэри!",
    "Почему коты всегда выигрывают в шахматы? Потому что они знают, как делать \"кошачьи\" ходы!"
]


PICS_DOGS = "https://masterpiecer-images.s3.yandex.net/9586e0deb07711ee8f9e5e02d8de8a56:upscaled"

PICS_CAT_ID = "AgACAgIAAxkDAAMvZ2al9YY1M9Rq2gZ3MWoFVLdx6EcAAqXiMRte7DhLC-GesOykAs0BAAMCAANtAAM2BA"

DONT_FORWARD_CONTENT = "Пожалуйста не пересылайте команды. Это может быть опасно!"

content_type_to_ru = {
    "text": "текст",
    "photo": "фото",
    "sticker": "стикер",
    "document": "документ",
}


MarkdownV2 = """*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
# comment
@bot.message_handler(commands=["md"])
def set_markdownV2(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=content.MarkdownV2,
        parse_mode="MarkdownV2"
    )
```
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity
>Expandable block quotation continued
>Hidden by default part of the expandable block quotation started
>Expandable block quotation continued
>The last line of the expandable block quotation with the expandability mark||
"""

