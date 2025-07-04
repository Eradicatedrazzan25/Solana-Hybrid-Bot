import asyncio
import os
from telegram import Bot

bot = Bot(token=os.getenv("BOT_TOKEN"))
chat_id = os.getenv("TARGET_CHAT_ID")

tracked = set()

async def check_mock_alert():
    token = {"name": "TestCoin", "address": "FAKE123"}
    if token['address'] not in tracked:
        tracked.add(token['address'])
        msg = f"🚨 New Token from @pfultimate\n\nName: {token['name']}\nAddress: {token['address']}"
        await bot.send_message(chat_id=chat_id, text=msg)

async def run_monitor():
    while True:
        await check_mock_alert()
        await asyncio.sleep(30)