from datetime import datetime

WORKOUTS = []


def add_workout(user_id: int, text: str) -> str:
    WORKOUTS.append({
        "user_id": user_id,
        "text": text,
        "date": datetime.now().isoformat()
    })

    return "💪 Тренировка сохранена"


def get_last_workouts(user_id: int) -> str:
    user_data = [w for w in WORKOUTS if w["user_id"] == user_id]

    if not user_data:
        return "📭 Тренировок пока нет"

    last = user_data[-5:]

    return "\n".join([
        f"{w['date'][:16]} — {w['text']}"
        for w in last
    ])