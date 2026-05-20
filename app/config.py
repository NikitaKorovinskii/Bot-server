import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

raw = os.getenv("ALLOWED_USER_IDS", "")

ALLOWED_USER_IDS = [
    int(x.strip())
    for x in raw.split(",")
    if x.strip().isdigit()
]

VPN_CONTAINERS = [
    "vpn-bot",
    "amnezia-xray",
    "mtproto-proxy",
    "amnezia-socks5proxy",
    "amnezia-awg"
]

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")