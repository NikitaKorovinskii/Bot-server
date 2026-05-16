from app.utils.keyboards import (
    main_menu,
    server_menu,
    server_status_menu,
    restart_menu,
    logs_menu,
    gym_menu,
)
from app.services.system_service import get_disk_usage, get_uptime
from app.services.docker_service import (
    get_container_status,
    restart_managed_containers,
    restart_container,
    get_container_logs,
)
from app.config import VPN_CONTAINERS
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


def render_server_status(bot, chat_id):
    bot.send_message(
        chat_id,
        "📊 Статус сервера",
        reply_markup=server_status_menu()
    )


def render_restart_containers(bot, chat_id):
    if not VPN_CONTAINERS:
        bot.send_message(chat_id, "Список контейнеров для перезапуска не настроен.")
        return

    bot.send_message(
        chat_id,
        "🔄 Выберите контейнер для перезапуска",
        reply_markup=restart_menu(VPN_CONTAINERS)
    )


def render_container_logs(bot, chat_id):
    if not VPN_CONTAINERS:
        bot.send_message(chat_id, "Список контейнеров для просмотра логов не настроен.")
        return

    bot.send_message(
        chat_id,
        "📄 Выберите контейнер для просмотра логов",
        reply_markup=logs_menu(VPN_CONTAINERS)
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

    elif action == "⏱️ Аптайм сервера":
        bot.send_message(chat_id, get_uptime())

    elif action == "🔄 Перезапустить контейнер":
        render_restart_containers(bot, chat_id)

    elif action == "📄 Логи контейнера":
        render_container_logs(bot, chat_id)

    else:
        if action.startswith("🔄 Перезапустить "):
            container_name = action.replace("🔄 Перезапустить ", "", 1)
            if container_name in VPN_CONTAINERS:
                bot.send_message(chat_id, restart_container(container_name))
                render_restart_containers(bot, chat_id)
                return

        if action.startswith("📄 Логи "):
            container_name = action.replace("📄 Логи ", "", 1)
            if container_name in VPN_CONTAINERS:
                bot.send_message(chat_id, get_container_logs(container_name))
                render_container_logs(bot, chat_id)
                return

        bot.send_message(chat_id, "❓ Команда не распознана. Используйте кнопки меню.")
