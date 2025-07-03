from telegram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")
bot = Bot(token=BOT_TOKEN)

def post_alert(msg):
    bot.send_message(chat_id=TARGET_CHAT_ID, text=msg)