from app.utils.auth import is_allowed
from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk, get_uptime
from app.services.docker_service import get_docker_status, restart_vpn
from app.services.gym_service import add_workout, get_last_workouts


def register(bot):

    @bot.message_handler(func=lambda m: True)
    def router(message):
        if not is_allowed(message):
            return

        text = message.text

        # MAIN MENU
        if text == "📦 Сервер":
            bot.send_message(message.chat.id, "📦 Сервер:", reply_markup=server_menu())

        elif text == "🏋️ Зал":
            bot.send_message(message.chat.id, "🏋️ Зал:", reply_markup=gym_menu())

        # SERVER
        elif text == "📊 Статус":
            bot.send_message(message.chat.id, get_docker_status())

        elif text == "💾 Диск":
            bot.send_message(message.chat.id, get_disk())

        elif text == "⏱ Аптайм":
            bot.send_message(message.chat.id, get_uptime())

        elif text == "🔄 VPN рестарт":
            bot.send_message(message.chat.id, restart_vpn())

        # GYM
        elif text.startswith("➕ Тренировка"):
            bot.send_message(message.chat.id, "Напиши: /workout <что сделал>")

        elif text == "📈 Прогресс":
            bot.send_message(message.chat.id, get_last_workouts(message.from_user.id))

        elif text == "⬅️ Назад":
            bot.send_message(message.chat.id, "🏠 Главное меню", reply_markup=main_menu())