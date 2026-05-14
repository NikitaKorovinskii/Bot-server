from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("🖥 Управление сервером", callback_data="menu_server")
    )

    kb.row(
        InlineKeyboardButton("🏋️ Тренировки", callback_data="menu_gym")
    )

    return kb


def server_menu():
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("📦 Состояние контейнеров", callback_data="srv_status")
    )

    kb.row(
        InlineKeyboardButton("🔄 Перезапустить контейнеры", callback_data="srv_restart")
    )

    kb.row(
        InlineKeyboardButton("💾 Место на сервере", callback_data="srv_disk")
    )

    kb.row(
        InlineKeyboardButton("⬅️ Назад", callback_data="back_main")
    )

    return kb


def gym_menu():
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("⬅️ Назад", callback_data="back_main")
    )

    return kb
