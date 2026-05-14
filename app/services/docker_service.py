import os

def get_docker_status():
    return os.popen("docker ps --format '{{.Names}} - {{.Status}}'").read()

def restart_vpn():
    return "VPN restarted (stub)"