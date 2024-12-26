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

html = """<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>

"""