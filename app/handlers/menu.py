from app.utils.auth import is_allowed
from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk, get_uptime
from app.services.docker_service import get_docker_status, restart_vpn
from app.services.gym_service import get_last_workouts


def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        if not is_allowed(message):
            return

        bot.send_message(
            message.chat.id,
            "🚀 Панель управления:",
            reply_markup=main_menu()
        )

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if not is_allowed(call.message):
            return

        data = call.data
        chat_id = call.message.chat.id

        print("🔥 CALLBACK:", data)

        # ⚠️ ОБЯЗАТЕЛЬНО — снимает "зависание кнопки"
        bot.answer_callback_query(call.id)

        if data == "menu_server":
            bot.edit_message_text(
                "📦 СЕРВЕР",
                chat_id,
                call.message.message_id,
                reply_markup=server_menu()
            )

        elif data == "menu_gym":
            bot.edit_message_text(
                "🏋️ ЗАЛ",
                chat_id,
                call.message.message_id,
                reply_markup=gym_menu()
            )

        elif data == "srv_status":
            bot.send_message(chat_id, get_docker_status())

        elif data == "srv_disk":
            bot.send_message(chat_id, get_disk())

        elif data == "srv_uptime":
            bot.send_message(chat_id, get_uptime())

        elif data == "srv_vpn":
            bot.send_message(chat_id, restart_vpn())

        elif data == "gym_progress":
            bot.send_message(chat_id, get_last_workouts(call.from_user.id))

        elif data == "gym_add":
            bot.send_message(chat_id, "Напиши: /workout ...")

        elif data == "back_main":
            bot.edit_message_text(
                "🚀 Панель управления:",
                chat_id,
                call.message.message_id,
                reply_markup=main_menu()
            )