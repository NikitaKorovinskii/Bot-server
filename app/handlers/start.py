from app.utils.auth import is_allowed
from app.utils.keyboards import main_menu


def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        if not is_allowed(message):
            return

        bot.send_message(
            message.chat.id,
            "🚀 Выбери раздел:",
            reply_markup=main_menu()
        )