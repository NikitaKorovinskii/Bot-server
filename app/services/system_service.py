import subprocess


def get_disk_usage() -> str:
    try:
        result = subprocess.run(
            ["df", "-h", "/"],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except Exception as exc:
        return f"Ошибка получения места на сервере: {exc}"

    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "неизвестная ошибка"
        return f"Не удалось получить место на сервере: {details}"

    output = result.stdout.strip() or "Нет данных"
    return f"Место на сервере:\n{output}"
