import telebot
import subprocess
import os

# env
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

bot = telebot.TeleBot(BOT_TOKEN)


# проверка доступа
def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS


# старт
@bot.message_handler(commands=['start'])
def start(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "VPN Bot готов 🚀")


# ping для теста CI/CD
@bot.message_handler(commands=['ping'])
def ping(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "pong 🟢 CI/CD работает")


# уведомление о деплое
def send_deploy_message():
    try:
        for user_id in ALLOWED_USER_IDS:
            bot.send_message(
                user_id,
                "🚀 Бот обновлён через CI/CD (deploy successful)"
            )
    except Exception as e:
        print("notify error:", e)


# запуск
if __name__ == "__main__":
    send_deploy_message()
    bot.infinity_polling()