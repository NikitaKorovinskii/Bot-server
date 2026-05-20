from telebot.types import ReplyKeyboardMarkup


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("🖥 Управление сервером")
    kb.row("🏋️ Тренировки")
    return kb


def server_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("📊 Статус сервера")
    kb.row("🔄 Перезапустить контейнер")
    kb.row("⬅️ Назад в главное меню")
    return kb


def server_status_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("📦 Состояние контейнеров")
    kb.row("💾 Место на сервере")
    kb.row("⏱️ Аптайм сервера")
    kb.row("📄 Логи контейнера")
    kb.row("⬅️ Назад в меню сервера")
    return kb


def restart_menu(containers):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for container in containers:
        kb.row(f"🔄 Перезапустить {container}")
    kb.row("⬅️ Назад в меню сервера")
    return kb


def logs_menu(containers):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for container in containers:
        kb.row(f"📄 Логи {container}")
    kb.row("⬅️ Назад в статус сервера")
    return kb


def gym_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    kb.row("⬅️ Назад в главное меню")
    return kb
