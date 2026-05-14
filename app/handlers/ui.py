from app.utils.keyboards import main_menu, server_menu, gym_menu
from app.services.system_service import get_disk, get_uptime
from app.services.docker_service import get_docker_status, restart_vpn
from app.services.gym_service import get_last_workouts


def render_main(bot, chat_id):
    bot.send_message(
        chat_id,
        "🚀 <b>ПАНЕЛЬ УПРАВЛЕНИЯ</b>",
        parse_mode="HTML",
        reply_markup=main_menu()
    )


def render_server(bot, call):
    bot.edit_message_text(
        "📦 <b>СЕРВЕР</b>",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=server_menu()
    )


def render_gym(bot, call):
    bot.edit_message_text(
        "🏋️ <b>ЗАЛ</b>",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=gym_menu()
    )


def action_server(bot, call, action):

    chat_id = call.message.chat.id

    bot.answer_callback_query(call.id)

    if action == "srv_status":
        bot.send_message(chat_id, get_docker_status())

    elif action == "srv_disk":
        bot.send_message(chat_id, get_disk())

    elif action == "srv_uptime":
        bot.send_message(chat_id, get_uptime())

    elif action == "srv_vpn":
        bot.send_message(chat_id, restart_vpn())

    elif action == "gym_progress":
        bot.send_message(chat_id, get_last_workouts(call.from_user.id))