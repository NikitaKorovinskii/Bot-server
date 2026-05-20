import logging
import os
import urllib.parse
from typing import Optional

import docker
from docker.errors import APIError, DockerException, NotFound

from app.config import VPN_CONTAINERS

logger = logging.getLogger(__name__)


def _normalize_docker_host(host: str) -> str:
    host = host.strip()
    if not host:
        return host

    parsed = urllib.parse.urlparse(host)
    scheme = parsed.scheme.lower()

    if scheme in ("http+docker", "https+docker"):
        parsed = parsed._replace(scheme="http" if scheme == "http+docker" else "https")
        return urllib.parse.urlunparse(parsed)

    if scheme == "unix":
        path = parsed.path
        if path.startswith("///"):
            path = path[2:]
        return f"unix://{path}"

    return host


def _get_client() -> tuple[Optional[docker.DockerClient], Optional[str]]:
    env = os.environ.copy()
    docker_host = env.get("DOCKER_HOST")
    if docker_host:
        env["DOCKER_HOST"] = _normalize_docker_host(docker_host)

    try:
        client = docker.from_env(environment=env)
        client.ping()
        return client, None
    except DockerException as exc:
        if os.path.exists("/var/run/docker.sock"):
            try:
                client = docker.DockerClient(base_url="unix://var/run/docker.sock")
                client.ping()
                return client, None
            except DockerException:
                pass

        error_msg = f"Не удалось подключиться к Docker: {exc}"
        logger.error(error_msg)
        return None, error_msg


def get_container_status() -> str:
    """Get status of all Docker containers using Docker SDK."""
    client, err = _get_client()
    if not client:
        return f"Состояние контейнеров:\n{err}"

    try:
        containers = client.containers.list(all=True)
        if not containers:
            return "Состояние контейнеров:\nНет контейнеров"

        lines = []
        for c in containers:
            try:
                c.reload()
                state = c.status
                status = c.attrs.get("State", {}).get("Status", "")
                lines.append(f"{c.name} - {state} ({status})")
            except Exception:
                lines.append(f"{c.name} - {getattr(c, 'status', 'unknown')}")

        return "Состояние контейнеров:\n" + "\n".join(lines)
    except DockerException as exc:
        logger.error("Ошибка при получении списка контейнеров: %s", exc)
        return f"Состояние контейнеров:\nОшибка: {exc}"


def restart_managed_containers() -> str:
    """Restart managed VPN containers using Docker SDK."""
    if not VPN_CONTAINERS:
        msg = "Список контейнеров для перезапуска не настроен."
        logger.warning(msg)
        return msg

    client, err = _get_client()
    if not client:
        return f"🔄 Перезапуск контейнеров:\n{err}"

    results = []
    for name in VPN_CONTAINERS:
        try:
            container = client.containers.get(name)
            container.restart()
            results.append(f"{name}: перезапущен")
        except NotFound:
            results.append(f"{name}: не найден")
        except APIError as exc:
            results.append(f"{name}: ошибка API: {exc}")
        except Exception as exc:
            results.append(f"{name}: ошибка: {exc}")

    return "🔄 Перезапуск контейнеров:\n" + "\n".join(results)


def restart_container(container_name: str) -> str:
    """Restart a single Docker container using Docker SDK."""
    if not container_name:
        msg = "Имя контейнера не указано."
        logger.warning(msg)
        return msg

    client, err = _get_client()
    if not client:
        return f"🔄 Перезапуск контейнера {container_name}:\n{err}"

    try:
        container = client.containers.get(container_name)
        container.restart()
        return f"🔄 Перезапуск контейнера {container_name}:\nУспешно"
    except NotFound:
        return f"Имя контейнера {container_name} не найдено."
    except Exception as exc:
        logger.error("Ошибка при перезапуске контейнера %s: %s", container_name, exc)
        return f"Ошибка при перезапуске контейнера {container_name}: {exc}"


def get_container_logs(container_name: str, tail: int = 20) -> str:
    """Get recent logs for a single Docker container using Docker SDK."""
    if not container_name:
        msg = "Имя контейнера не указано."
        logger.warning(msg)
        return msg

    client, err = _get_client()
    if not client:
        return f"📄 Логи контейнера {container_name} (последние {tail} строк):\n{err}"

    try:
        container = client.containers.get(container_name)
        logs = container.logs(tail=tail, stdout=True, stderr=True)
        if isinstance(logs, bytes):
            logs = logs.decode(errors="replace")
        return f"📄 Логи контейнера {container_name} (последние {tail} строк):\n{logs or 'Нет данных'}"
    except NotFound:
        return f"Имя контейнера {container_name} не найдено."
    except Exception as exc:
        logger.error("Ошибка при получении логов контейнера %s: %s", container_name, exc)
        return f"Ошибка получения логов контейнера: {exc}"
