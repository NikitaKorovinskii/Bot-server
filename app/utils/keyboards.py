from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    print("🔥 main_menu:")
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("📦 Сервер", callback_data="menu_server"),
        InlineKeyboardButton("🏋️ Зал", callback_data="menu_gym")
    )

    return kb


def server_menu():
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("📊 Статус", callback_data="srv_status"),
        InlineKeyboardButton("💾 Диск", callback_data="srv_disk")
    )

    kb.row(
        InlineKeyboardButton("⏱ Аптайм", callback_data="srv_uptime"),
        InlineKeyboardButton("🔄 VPN", callback_data="srv_vpn")
    )

    kb.row(
        InlineKeyboardButton("⬅️ Назад", callback_data="back_main")
    )

    return kb


def gym_menu():
    kb = InlineKeyboardMarkup()

    kb.row(
        InlineKeyboardButton("📈 Прогресс", callback_data="gym_progress")
    )

    kb.row(
        InlineKeyboardButton("⬅️ Назад", callback_data="back_main")
    )

    return kb