from app.utils.auth import is_allowed
from app.texts.messages import HELP_TEXT

def register(bot):

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