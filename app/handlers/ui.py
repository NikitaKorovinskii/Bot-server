from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk, get_uptime
from app.services.docker_service import get_docker_status, restart_vpn


# -------------------------
# SCREENS
# -------------------------

def render_main(bot, chat_id):
    bot.send_message(
        chat_id,
        "🚀 ПАНЕЛЬ УПРАВЛЕНИЯ",
        reply_markup=main_menu()
    )


def render_server(bot, call):
    bot.edit_message_text(
        "📦 СЕРВЕР",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=server_menu()
    )


def render_gym(bot, call):
    bot.edit_message_text(
        "🏋️ ЗАЛ",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=gym_menu()
    )


# -------------------------
# SERVER ACTIONS
# -------------------------

def action_server(bot, call, action):

    chat_id = call.message.chat.id

    if action == "srv_status":
        bot.send_message(chat_id, get_docker_status())

    elif action == "srv_disk":
        bot.send_message(chat_id, get_disk())

    elif action == "srv_uptime":
        bot.send_message(chat_id, get_uptime())

    elif action == "srv_vpn":
        bot.send_message(chat_id, restart_vpn())