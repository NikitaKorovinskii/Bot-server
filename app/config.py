import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

raw = os.getenv("ALLOWED_USER_IDS", "")

ALLOWED_USER_IDS = [
    int(x.strip())
    for x in raw.split(",")
    if x.strip().isdigit()
]

VPN_CONTAINERS = [
    "amnezia-awg",
    "amnezia-socks5proxy"
]