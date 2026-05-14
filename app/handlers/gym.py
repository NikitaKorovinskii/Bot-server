from app.utils.auth import is_allowed
from app.utils.keyboards import gym_menu
from app.services.gym_service import add_workout, get_last_workouts


def register(bot):

    @bot.message_handler(func=lambda m: True)
    def gym_router(message):
        if not is_allowed(message):
            return

        text = message.text

        if text == "➕ Тренировка":
            bot.send_message(
                message.chat.id,
                "Напиши тренировку в формате:\n/workout bench press 80kg"
            )

        elif text == "📈 Прогресс":
            bot.send_message(
                message.chat.id,
                get_last_workouts(message.from_user.id)
            )