import subprocess
import logging

from app.config import VPN_CONTAINERS

logger = logging.getLogger(__name__)


def _run_command(command: list[str]) -> str:
    """Execute a shell command and return output."""
    try:
        logger.debug(f"Executing command: {' '.join(command)}")
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        error_msg = "Команда превышена по времени (timeout)"
        logger.error(error_msg)
        return f"Ошибка: {error_msg}"
    except Exception as exc:
        error_msg = f"Ошибка выполнения команды: {exc}"
        logger.error(error_msg, exc_info=True)
        return error_msg

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    if result.returncode != 0:
        details = stderr or stdout or "неизвестная ошибка"
        error_msg = f"Команда завершилась с ошибкой: {details}"
        logger.error(error_msg)
        return error_msg

    output = stdout or "Нет данных"
    logger.info(f"Command executed successfully: {' '.join(command)}")
    return output


def get_container_status() -> str:
    """Get status of all Docker containers."""
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
    """Restart managed VPN containers."""
    if not VPN_CONTAINERS:
        msg = "Список контейнеров для перезапуска не настроен."
        logger.warning(msg)
        return msg

    output = _run_command(["docker", "restart", *VPN_CONTAINERS])
    return f"Перезапуск контейнеров:\n{output}"


def restart_container(container_name: str) -> str:
    """Restart a single Docker container."""
    if not container_name:
        return "Имя контейнера не указано."

    output = _run_command(["docker", "restart", container_name])
    return f"Перезапуск контейнера {container_name}:\n{output}"


def get_container_logs(container_name: str, tail: int = 20) -> str:
    """Get recent logs for a single Docker container."""
    if not container_name:
        return "Имя контейнера не указано."

    output = _run_command(["docker", "logs", "--tail", str(tail), container_name])
    return f"Логи контейнера {container_name} (последние {tail} строк):\n{output}"
