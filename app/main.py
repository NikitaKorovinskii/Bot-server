import telebot
from app.config import BOT_TOKEN
from app.handlers import register_all

print("🚀 BOT STARTING")

bot = telebot.TeleBot(BOT_TOKEN)

register_all(bot)

print("🚀 HANDLERS LOADED")

bot.infinity_polling(
    skip_pending=True,
    timeout=60,
    long_polling_timeout=60
)