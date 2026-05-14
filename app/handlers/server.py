from app.utils.auth import is_allowed
from app.services.system_service import get_docker_status, get_disk, get_uptime
from app.services.docker_service import restart_vpn

def register(bot):

    @bot.message_handler(commands=['status'])
    def status(message):
        if not is_allowed(message):
            return
        bot.reply_to(message, get_docker_status())

    @bot.message_handler(commands=['disk'])
    def disk(message):
        if not is_allowed(message):
            return
        bot.reply_to(message, get_disk())

    @bot.message_handler(commands=['uptime'])
    def uptime(message):
        if not is_allowed(message):
            return
        bot.reply_to(message, get_uptime())

    @bot.message_handler(commands=['restart_vpn'])
    def restart(message):
        if not is_allowed(message):
            return
        bot.reply_to(message, restart_vpn())