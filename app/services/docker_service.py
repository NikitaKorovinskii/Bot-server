import docker
from app.config import VPN_CONTAINERS

client = docker.from_env()

def restart_vpn():
    logs = []

    for name in VPN_CONTAINERS:
        try:
            container = client.containers.get(name)
            container.restart()
            logs.append(f"✅ {name}")
        except Exception as e:
            logs.append(f"❌ {name}: {e}")

    return "\n".join(logs)