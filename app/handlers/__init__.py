print("HANDLERS INIT STARTED")

from app.handlers.menu import register as register_menu


def register_all(bot):
    print("REGISTER_ALL CALLED")
    register_menu(bot)