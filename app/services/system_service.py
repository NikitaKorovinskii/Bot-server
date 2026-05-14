import os

def get_docker_status():
    return os.popen("docker ps --format '{{.Names}} - {{.Status}}'").read()

def get_disk():
    return os.popen("df -h /").read()

def get_uptime():
    return os.popen("uptime").read()