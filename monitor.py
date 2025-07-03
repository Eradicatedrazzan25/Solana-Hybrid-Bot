import asyncio
import os
from telegram import Bot

bot_token = os.getenv("BOT_TOKEN")
target_chat_id = os.getenv("TARGET_CHAT_ID")
bot = Bot(token=bot_token)

tracked = set()

async def check_pfultimate():
    # Simulate a new token call
    new_token = {
        "name": "Meowcoin",
        "address": "G9F...XYZ"
    }
    token_key = new_token["address"]
    if token_key not in tracked:
        tracked.add(token_key)
        msg = f"🚨 New Token from @pfultimate\n\nName: {new_token['name']}\nAddress: {new_token['address']}\n\n#pumpfun"
        await bot.send_message(chat_id=target_chat_id, text=msg)

async def run_monitor():
    while True:
        await check_pfultimate()
        await asyncio.sleep(30)