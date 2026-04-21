import telebot
import os
import docker

# env
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

bot = telebot.TeleBot(BOT_TOKEN)

client = docker.from_env()

# whitelist контейнеров (ВАЖНО)
VPN_CONTAINERS = [
    "amnezia-awg",
    "amnezia-socks5proxy"
]


def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS


HELP_TEXT = """
🤖 Управление сервером:

/ping — проверка бота
/status — контейнеры Docker
/disk — место на диске
/uptime — аптайм сервера
/restart_vpn — перезапуск VPN
"""


@bot.message_handler(commands=['start'])
def start(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, f"🚀 VPN Bot готов\n{HELP_TEXT}")


@bot.message_handler(commands=['help'])
def help_cmd(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, HELP_TEXT)


@bot.message_handler(commands=['ping'])
def ping(message):
    if not is_allowed(message):
        return
    bot.reply_to(message, "pong")


@bot.message_handler(commands=['status'])
def status(message):
    if not is_allowed(message):
        return
    result = os.popen("docker ps --format '{{.Names}} - {{.Status}}'").read()
    bot.reply_to(message, f"📦 Контейнеры:\n{result}")


@bot.message_handler(commands=['disk'])
def disk(message):
    if not is_allowed(message):
        return
    result = os.popen("df -h /").read()
    bot.reply_to(message, f"💾 Диск:\n{result}")


@bot.message_handler(commands=['uptime'])
def uptime(message):
    if not is_allowed(message):
        return
    result = os.popen("uptime").read()
    bot.reply_to(message, f"⏱ Аптайм:\n{result}")


@bot.message_handler(commands=['restart_vpn'])
def restart_vpn(message):
    if not is_allowed(message):
        return

    logs = []

    for name in VPN_CONTAINERS:
        try:
            container = client.containers.get(name)
            container.restart()
            logs.append(f"✅ {name}")
        except Exception as e:
            logs.append(f"❌ {name}: {str(e)}")

    bot.reply_to(message, "🔄 VPN restart:\n" + "\n".join(logs))


if __name__ == "__main__":
    bot.infinity_polling()