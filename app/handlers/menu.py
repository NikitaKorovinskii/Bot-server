from app.utils.auth import is_allowed
from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk, get_uptime
from app.services.docker_service import get_docker_status, restart_vpn
from app.services.gym_service import get_last_workouts


def register(bot):

    @bot.message_handler(func=lambda m: True)
    def router(message):
        if not is_allowed(message):
            return

        text = (message.text or "").strip()

        print("DEBUG:", repr(text))

        # MAIN MENU
        if "Сервер" in text:
            bot.send_message(
                message.chat.id,
                "📦 Сервер:",
                reply_markup=server_menu()
            )

        elif "Зал" in text:
            bot.send_message(
                message.chat.id,
                "🏋️ Зал:",
                reply_markup=gym_menu()
            )

        # SERVER ACTIONS
        elif "Статус" in text:
            bot.send_message(message.chat.id, get_docker_status())

        elif "Диск" in text:
            bot.send_message(message.chat.id, get_disk())

        elif "Аптайм" in text:
            bot.send_message(message.chat.id, get_uptime())

        elif "VPN" in text:
            bot.send_message(message.chat.id, restart_vpn())

        # GYM
        elif "Прогресс" in text:
            bot.send_message(
                message.chat.id,
                get_last_workouts(message.from_user.id)
            )

        elif "Тренировка" in text:
            bot.send_message(
                message.chat.id,
                "Напиши:\n/workout <что сделал>"
            )

        # BACK
        elif "Назад" in text:
            bot.send_message(
                message.chat.id,
                "🏠 Главное меню",
                reply_markup=main_menu()
            )