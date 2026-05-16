import subprocess
import logging

logger = logging.getLogger(__name__)


def get_disk_usage() -> str:
    """Get disk usage information for root partition."""
    try:
        logger.debug("Fetching disk usage information")
        result = subprocess.run(
            ["df", "-h", "/"],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except subprocess.TimeoutExpired:
        error_msg = "Ошибка получения места на сервере: timeout"
        logger.error(error_msg)
        return error_msg
    except Exception as exc:
        error_msg = f"Ошибка получения места на сервере: {exc}"
        logger.error(error_msg, exc_info=True)
        return error_msg

    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "неизвестная ошибка"
        error_msg = f"Не удалось получить место на сервере: {details}"
        logger.error(error_msg)
        return error_msg

    output = result.stdout.strip() or "Нет данных"
    logger.info("Disk usage fetched successfully")
    return f"Место на сервере:\n{output}"



def get_uptime() -> str:
    """Get server uptime."""
    try:
        logger.debug("Fetching server uptime")
        result = subprocess.run(
            ["uptime", "-p"],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except subprocess.TimeoutExpired:
        error_msg = "Ошибка получения времени работы сервера: timeout"
        logger.error(error_msg)
        return error_msg
    except Exception as exc:
        error_msg = f"Ошибка получения времени работы сервера: {exc}"
        logger.error(error_msg, exc_info=True)
        return error_msg

    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "неизвестная ошибка"
        error_msg = f"Не удалось получить аптайм: {details}"
        logger.error(error_msg)
        return error_msg

    output = result.stdout.strip() or "Нет данных"
    logger.info("Server uptime fetched successfully")
    return f"Аптайм сервера:\n{output}"
