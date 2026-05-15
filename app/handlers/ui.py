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
        "📋 Главное меню",
        reply_markup=main_menu()
    )


def render_server(bot, chat_id):
    bot.send_message(
        chat_id,
        "🖥 Раздел: управление сервером",
        reply_markup=server_menu()
    )


def render_gym(bot, chat_id):
    bot.send_message(
        chat_id,
        get_gym_section_message(),
        reply_markup=gym_menu()
    )


# -------------------------
# SERVER ACTIONS
# -------------------------

def action_server(bot, chat_id, action):
    if action == "📦 Состояние контейнеров":
        bot.send_message(chat_id, get_container_status())

    elif action == "💾 Место на сервере":
        bot.send_message(chat_id, get_disk_usage())

    elif action == "🔄 Перезапустить контейнеры":
        bot.send_message(chat_id, restart_managed_containers())
