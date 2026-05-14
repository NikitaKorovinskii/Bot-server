import os

ALLOWED_USER_IDS = [
    int(x) for x in os.getenv("ALLOWED_USER_IDS", "").split(",") if x
]

def is_allowed(message):
    return message.from_user.id in ALLOWED_USER_IDS