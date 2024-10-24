import os
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


class TelegramBot:
    def __init__(self):
        self.chat_ids = []
        self.token = os.getenv("BOT_TOKEN")
        if not self.token:
            raise EnvironmentError("Cannot access telegram bot token")

    async def add_chat_id(self, chat_id: str):
        self.chat_ids.append(chat_id)

    async def send_messages(self, message: str):
        for chat_id in self.chat_ids:
            async with Bot(token=self.token, default=DefaultBotProperties(
                    parse_mode=ParseMode.HTML,
            ),
                           ) as bot:
                await bot.send_message(chat_id=chat_id, text=message)
        print(">>> telegram messages have been sent")
