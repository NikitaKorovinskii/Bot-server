from app.utils.auth import is_allowed
from app.services.gym_service import add_workout, get_last_workouts


def register(bot):

    @bot.message_handler(commands=['workout'])
    def workout_cmd(message):
        if not is_allowed(message):
            return

        text = message.text.replace("/workout", "").strip()

        if not text:
            bot.send_message(message.chat.id, "Напиши: /workout жим 80кг")
            return

        bot.send_message(message.chat.id, add_workout(message.from_user.id, text))


    @bot.message_handler(commands=['progress'])
    def progress_cmd(message):
        if not is_allowed(message):
            return

        bot.send_message(message.chat.id, get_last_workouts(message.from_user.id))