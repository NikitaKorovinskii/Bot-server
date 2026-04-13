import telebot
import subprocess
import os

# env
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

print("🚀 DEPLOY TEST: BOT STARTED")

bot = telebot.TeleBot(BOT_TOKEN)


# проверка доступа
def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS


# старт
@bot.message_handler(commands=['start'])
def start(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "VPN Bot готов 🚀\n/ping /status /disk /uptime")


# ping CI/CD
@bot.message_handler(commands=['ping'])
def ping(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "pong 🟢 CI/CD работает")


# docker status
@bot.message_handler(commands=['status'])
def status(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("docker ps --format '{{.Names}} - {{.Status}}'")
    bot.reply_to(message, f"📦 Docker containers:\n{result}")


# disk usage
@bot.message_handler(commands=['disk'])
def disk(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("df -h /")
    bot.reply_to(message, f"💾 Disk usage:\n{result}")


# uptime
@bot.message_handler(commands=['uptime'])
def uptime(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("uptime")
    bot.reply_to(message, f"⏱ Server uptime:\n{result}")


# restart VPN containers
@bot.message_handler(commands=['restart_vpn'])
def restart_vpn(message):
    if not is_allowed(message):
        return
    subprocess.run("docker restart amnezia-awg amnezia-socks5proxy", shell=True)
    bot.reply_to(message, "🔄 VPN containers restarted")


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