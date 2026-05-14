from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk_usage
from app.services.docker_service import get_container_status, restart_managed_containers
from app.services.gym_service import get_gym_section_message


# -------------------------
# SCREENS
# -------------------------

def render_main(bot, chat_id):
    bot.send_message(
        chat_id,
        "Главное меню",
        reply_markup=main_menu()
    )


def render_server(bot, call):
    bot.edit_message_text(
        "Раздел: управление сервером",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=server_menu()
    )


def render_gym(bot, call):
    bot.edit_message_text(
        get_gym_section_message(),
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
        bot.send_message(chat_id, get_container_status())

    elif action == "srv_disk":
        bot.send_message(chat_id, get_disk_usage())

    elif action == "srv_restart":
        bot.send_message(chat_id, restart_managed_containers())
