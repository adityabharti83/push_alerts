from twilio.rest import Client
from .utils import logger
from .config import Config

client = Client(Config.TWILIO_SID, Config.TWILIO_AUTH_TOKEN)

def send_sms(to_number, message):
    try:
        response = client.messages.create(
            body=message, from_=Config.TWILIO_PHONE_NUMBER, to=to_number
        )
        logger.info(f"SMS sent: {response.sid}")
        return response.sid
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}")
