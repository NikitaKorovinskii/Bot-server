import os

raw = os.getenv("ALLOWED_USER_IDS", "")

ALLOWED_USER_IDS = [
    int(x.strip())
    for x in raw.split(",")
    if x.strip().isdigit()
]


def is_allowed(user_id: int) -> bool:
    return user_id in ALLOWED_USER_IDS