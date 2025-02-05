import requests
from .config import Config
from .utils import logger

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info(f"Telegram message sent: {response.json()}")
        return response.json()
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")
