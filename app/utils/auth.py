from app.config import ALLOWED_USER_IDS

def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS