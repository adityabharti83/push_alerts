import firebase_admin
from firebase_admin import messaging, credentials
from .utils import logger
from .config import Config

cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body, data=None):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        data=data or {},
        token=token
    )
    response = messaging.send(message)
    logger.info(f"Push notification sent: {response}")
    return response
