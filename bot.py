import telebot
import subprocess
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

bot = telebot.TeleBot(BOT_TOKEN)

def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS


@bot.message_handler(commands=['start'])
def start(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "VPN Bot готов 🚀")


# 🔥 функция уведомления о деплое
def send_deploy_message():
    try:
        for user_id in ALLOWED_USER_IDS:
            bot.send_message(user_id, "🚀 Бот обновлён через CI/CD (git push detected)")
    except Exception as e:
        print("notify error:", e)


# вызываем при старте контейнера
send_deploy_message()

bot.infinity_polling()