import telebot
import logging
import signal
from app.config import BOT_TOKEN, LOG_LEVEL
from app.handlers.router import register_router

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(BOT_TOKEN)
register_router(bot)


def signal_handler(sig, frame):
    """Handle graceful shutdown."""
    logger.info("🛑 Bot shutting down gracefully...")
    logger.info("✅ Bot stopped")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    logger.info("🚀 BOT STARTED")
    try:
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"❌ Bot error: {e}", exc_info=True)
        raise