import subprocess

from app.config import VPN_CONTAINERS


def _run_command(command: list[str]) -> str:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except Exception as exc:
        return f"Ошибка выполнения команды: {exc}"

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    if result.returncode != 0:
        details = stderr or stdout or "неизвестная ошибка"
        return f"Команда завершилась с ошибкой: {details}"

    return stdout or "Нет данных"


def get_container_status() -> str:
    output = _run_command(
        [
            "docker",
            "ps",
            "-a",
            "--format",
            "{{.Names}} - {{.State}} ({{.Status}})",
        ]
    )
    return f"Состояние контейнеров:\n{output}"


def restart_managed_containers() -> str:
    if not VPN_CONTAINERS:
        return "Список контейнеров для перезапуска не настроен."

    output = _run_command(["docker", "restart", *VPN_CONTAINERS])
    return f"Перезапуск контейнеров:\n{output}"
