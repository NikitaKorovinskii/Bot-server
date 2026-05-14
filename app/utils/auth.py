import os

ALLOWED_USER_IDS = [
    int(x) for x in os.getenv("ALLOWED_USER_IDS", "").split(",") if x
]

def is_allowed_user(user_id: int):
    return user_id in ALLOWED_USER_IDS