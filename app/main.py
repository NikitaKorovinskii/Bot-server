import telebot
from app.config import BOT_TOKEN
from app.handlers import register_all

print("🚀 BOT STARTING")

bot = telebot.TeleBot(BOT_TOKEN)

register_all(bot)

print("🚀 BOT READY")

if __name__ == "__main__":
    bot.infinity_polling()