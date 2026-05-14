from app.handlers.start import register as register_start
from app.handlers.server import register as register_server

def register_all(bot):
    register_start(bot)
    register_server(bot)