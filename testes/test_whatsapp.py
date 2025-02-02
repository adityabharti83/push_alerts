import pytest
from push_alerts import send_whatsapp_message

def test_send_whatsapp_message():
    dummy_phone = "+1234567890"
    response = send_whatsapp_message(dummy_phone, "Test notification")
    assert response is not None
