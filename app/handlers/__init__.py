from app.handlers.start import register as register_start
from app.handlers.server import register as register_server
from app.handlers.gym import register as register_gym
from app.handlers.menu import register as register_menu


def register_all(bot):
    register_start(bot)
    register_server(bot)
    register_gym(bot)
    register_menu(bot)