from app.utils.auth import is_allowed
from app.handlers.ui import render_main, render_server, render_gym
from app.handlers.ui import action_server
from app.utils.keyboards import main_menu


def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        if not is_allowed(message):
            return

        render_main(bot, message.chat.id)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        print("🔥 CALLBACK RECEIVED:", call.data)
        if not is_allowed(call.message):
            return

        data = call.data
        chat_id = call.message.chat.id

        print("🔥 CALLBACK:", data)

        # NAVIGATION
        if data == "menu_server":
            render_server(bot, call)

        elif data == "menu_gym":
            render_gym(bot, call)

        elif data == "back_main":
            bot.edit_message_text(
                "🚀 ПАНЕЛЬ УПРАВЛЕНИЯ",
                chat_id,
                call.message.message_id,
                reply_markup=main_menu()
            )

        # SERVER ACTIONS
        elif data in ["srv_status", "srv_disk", "srv_uptime", "srv_vpn"]:
            action_server(bot, call, data)

        # GYM ACTIONS
        elif data == "gym_progress":
            action_server(bot, call, data)