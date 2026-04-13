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


# help
HELP_TEXT = """
🤖 Управление сервером:

/ping — проверка бота
/status — контейнеры Docker
/disk — место на диске
/uptime — аптайм сервера
/restart_vpn — перезапуск VPN
"""


# старт
@bot.message_handler(commands=['start'])
def start(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, f"🚀 VPN Bot готов\n{HELP_TEXT}")


# help
@bot.message_handler(commands=['help'])
def help_cmd(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, HELP_TEXT)


# ping
@bot.message_handler(commands=['ping'])
def ping(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "🟢 Бот работает (CI/CD ок)")


# docker status
@bot.message_handler(commands=['status'])
def status(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("docker ps --format '{{.Names}} - {{.Status}}'")
    bot.reply_to(message, f"📦 Контейнеры Docker:\n{result}")


# disk usage
@bot.message_handler(commands=['disk'])
def disk(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("df -h /")
    bot.reply_to(message, f"💾 Использование диска:\n{result}")


# uptime
@bot.message_handler(commands=['uptime'])
def uptime(message):
    if not is_allowed(message):
        return
    result = subprocess.getoutput("uptime")
    bot.reply_to(message, f"⏱ Аптайм сервера:\n{result}")


# restart VPN
@bot.message_handler(commands=['restart_vpn'])
def restart_vpn(message):
    if not is_allowed(message):
        return
    subprocess.run("docker restart amnezia-awg amnezia-socks5proxy", shell=True)
    bot.reply_to(message, "🔄 VPN контейнеры перезапущены")


# запуск
if __name__ == "__main__":
    bot.infinity_polling()