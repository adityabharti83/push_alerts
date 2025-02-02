import pytest
from push_alerts import send_telegram_message

def test_send_telegram_message():
    dummy_chat_id = "123456789"
    response = send_telegram_message(dummy_chat_id, "Test notification")
    assert response is not None
