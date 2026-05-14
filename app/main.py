import telebot
from app.config import BOT_TOKEN
from app.handlers import register_all

bot = telebot.TeleBot(BOT_TOKEN)

register_all(bot)

if __name__ == "__main__":
    print("BOT STARTED")
    bot.infinity_polling()