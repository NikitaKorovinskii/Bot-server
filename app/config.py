import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

ALLOWED_USER_IDS = [
    int(x.strip())
    for x in os.getenv("ALLOWED_USER_IDS", "").split(",")
    if x.strip()
]

VPN_CONTAINERS = [
    "amnezia-awg",
    "amnezia-socks5proxy"
]