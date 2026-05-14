import os

def get_disk():
    return os.popen("df -h /").read()

def get_uptime():
    return os.popen("uptime").read()