from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row(
        KeyboardButton("📦 Сервер"),
        KeyboardButton("🏋️ Зал")
    )

    return kb


def server_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("📊 Статус", "💾 Диск")
    kb.row("⏱ Аптайм", "🔄 VPN рестарт")
    kb.row("⬅️ Назад")

    return kb


def gym_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("➕ Тренировка", "📈 Прогресс")
    kb.row("⬅️ Назад")

    return kb