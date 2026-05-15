from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("🖥 Управление сервером")
    kb.row("🏋️ Тренировки")
    return kb


def server_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("📦 Состояние контейнеров")
    kb.row("🔄 Перезапустить контейнеры")
    kb.row("💾 Место на сервере")
    kb.row("⬅️ Назад в главное меню")
    return kb


def gym_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("⬅️ Назад в главное меню")
    return kb
