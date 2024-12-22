import os
import json
from dotenv import load_dotenv
from telebot import types
from telebot.custom_filters import (
    SimpleCustomFilter,
)


load_dotenv()
id_admins = os.getenv('ID_ADMINS')
id_admins_lst = json.loads(id_admins)

class IsUserBotAdmin(SimpleCustomFilter):
    key = "is_user_bot_admin"
    
    def check(self, message: types.Message):
        return message.from_user.id in id_admins_lst


if __name__ == "__main__":
    pass
