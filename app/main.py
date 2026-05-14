import telebot
from app.config import BOT_TOKEN
from app.handlers.router import register_router

bot = telebot.TeleBot(BOT_TOKEN)

register_router(bot)

if __name__ == "__main__":
    print("🚀 BOT STARTED")
    bot.infinity_polling()