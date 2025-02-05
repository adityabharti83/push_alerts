from fastapi import APIRouter
from .utils import logger

webhook_listener = APIRouter()

@webhook_listener.post("/webhook")
async def receive_webhook(payload: dict):
    logger.info(f"Received webhook: {payload}")
    return {"status": "received"}
