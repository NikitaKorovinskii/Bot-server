import docker

client = docker.from_env()

VPN_CONTAINERS = [
    "amnezia-awg",
    "amnezia-socks5proxy"
]


def get_docker_status() -> str:
    return "\n".join([
        f"{c.name} - {c.status}"
        for c in client.containers.list(all=True)
    ])


def restart_vpn() -> str:
    logs = []

    for name in VPN_CONTAINERS:
        try:
            container = client.containers.get(name)
            container.restart()
            logs.append(f"✅ {name}")
        except Exception as e:
            logs.append(f"❌ {name}: {str(e)}")

    return "\n".join(logs)