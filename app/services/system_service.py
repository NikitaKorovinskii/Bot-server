import subprocess


def run(cmd: str) -> str:
    return subprocess.getoutput(cmd)


def get_disk() -> str:
    return run("df -h /")


def get_uptime() -> str:
    return run("uptime")