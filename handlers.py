import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Hybrid Solana Bot is running!
Use /status or /settings to continue.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Currently monitoring alpha sources.
Auto-buy/sell: enabled.")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

async def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)
    print("✅ Telegram bot running.")
    await app.run_polling()