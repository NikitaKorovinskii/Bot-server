from app.utils.auth import is_allowed
from app.handlers.ui import (
    render_main,
    render_server,
    render_gym,
    action_server
)
from app.utils.keyboards import main_menu
from app.services.gym_service import get_last_workouts


def register_router(bot):

    print("🔥 ROUTER LOADED")

    # -------------------------
    # START
    # -------------------------
    @bot.message_handler(commands=['start'])
    def start(message):
        if not is_allowed(message):
            return

        render_main(bot, message.chat.id)

    # -------------------------
    # CALLBACKS
    # -------------------------
    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):

        print("🔥 CALLBACK:", call.data)

        # ❌ ДОСТУП
        if not is_allowed(call.from_user):
            bot.answer_callback_query(
                call.id,
                "⛔ Нет доступа",
                show_alert=True
            )
            return

        data = call.data

        bot.answer_callback_query(call.id)

        # -------------------------
        # NAVIGATION
        # -------------------------
        if data == "menu_server":
            render_server(bot, call)

        elif data == "menu_gym":
            render_gym(bot, call)

        elif data == "back_main":
            bot.edit_message_text(
                "🚀 ПАНЕЛЬ УПРАВЛЕНИЯ",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=main_menu()
            )

        # -------------------------
        # SERVER ACTIONS
        # -------------------------
        elif data in ["srv_status", "srv_disk", "srv_uptime", "srv_vpn"]:
            action_server(bot, call, data)

        # -------------------------
        # GYM
        # -------------------------
        elif data == "gym_progress":
            bot.send_message(
                call.message.chat.id,
                get_last_workouts(call.from_user.id)
            )