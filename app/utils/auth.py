from app.config import ALLOWED_USER_IDS


def is_allowed(user_id: int) -> bool:
    """Check if user ID is in the allowed list."""
    return user_id in ALLOWED_USER_IDS