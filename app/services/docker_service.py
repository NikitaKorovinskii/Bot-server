import logging
import os
import subprocess
from typing import Optional

from app.config import VPN_CONTAINERS

logger = logging.getLogger(__name__)


def _run_docker_command(command: list[str], timeout: int = 30) -> str:
    env = os.environ.copy()
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            env=env,
            check=False,
            timeout=timeout,
        )
    except FileNotFoundError:
        error_msg = "docker CLI не найден. Установите docker внутри образа."
        logger.error(error_msg)
        return f"Ошибка выполнения команды: {error_msg}"
    except subprocess.TimeoutExpired:
        error_msg = "Команда превышена по времени (timeout)"
        logger.error(error_msg)
        return f"Ошибка выполнения команды: {error_msg}"
    except Exception as exc:
        error_msg = f"Ошибка выполнения команды: {exc}"
        logger.error(error_msg, exc_info=True)
        return error_msg

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    if result.returncode != 0:
        details = stderr or stdout or "неизвестная ошибка"
        error_msg = f"Команда завершилась с ошибкой: {details}"
        logger.error("Docker CLI error: %s", details)
        return error_msg

    return stdout or "Нет данных"


def get_container_status() -> str:
    output = _run_docker_command(
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
        msg = "Список контейнеров для перезапуска не настроен."
        logger.warning(msg)
        return msg

    output = _run_docker_command(["docker", "restart", *VPN_CONTAINERS])
    return f"🔄 Перезапуск контейнеров:\n{output}"


def restart_container(container_name: str) -> str:
    if not container_name:
        msg = "Имя контейнера не указано."
        logger.warning(msg)
        return msg

    output = _run_docker_command(["docker", "restart", container_name])
    return f"🔄 Перезапуск контейнера {container_name}:\n{output}"


def get_container_logs(container_name: str, tail: int = 20) -> str:
    if not container_name:
        msg = "Имя контейнера не указано."
        logger.warning(msg)
        return msg

    output = _run_docker_command(
        ["docker", "logs", "--tail", str(tail), container_name]
    )
    return f"📄 Логи контейнера {container_name} (последние {tail} строк):\n{output}"



