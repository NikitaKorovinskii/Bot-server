import logging
from app.utils.auth import is_allowed
from app.handlers.ui import render_main, render_server, render_gym, action_server
from app.utils.keyboards import main_menu

logger = logging.getLogger(__name__)


def register_router(bot):
    logger.info("🔥 ROUTER LOADED")

    # -------------------------
    # START
    # -------------------------
    @bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.from_user.id
        if not is_allowed(user_id):
            logger.warning(f"⛔ Unauthorized access attempt from user {user_id}")
            bot.reply_to(message, "⛔ У вас нет доступа к этому боту")
            return

        logger.info(f"✅ User {user_id} started bot")
        render_main(bot, message.chat.id)

    # -------------------------
    # TEXT MESSAGES
    # -------------------------
    @bot.message_handler(func=lambda message: True)
    def handle_text(message):
        user_id = message.from_user.id
        if not is_allowed(user_id):
            logger.warning(f"⛔ Unauthorized access attempt from user {user_id}")
            bot.reply_to(message, "⛔ У вас нет доступа к этому боту")
            return

        text = message.text
        chat_id = message.chat.id
        logger.info(f"📬 Message from user {user_id}: {text}")

        # Main menu actions
        if text == "🖥 Управление сервером":
            render_server(bot, chat_id)

        elif text == "🏋️ Тренировки":
            render_gym(bot, chat_id)

        # Server menu actions
        elif text in ["📦 Состояние контейнеров", "🔄 Перезапустить контейнеры", "💾 Место на сервере"]:
            action_server(bot, chat_id, text)

        # Back to main menu
        elif text == "⬅️ Назад в главное меню":
            render_main(bot, chat_id)

        else:
            bot.reply_to(message, "❓ Команда не распознана. Используйте кнопки меню.")
