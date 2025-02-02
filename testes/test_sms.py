import pytest
from push_alerts import send_sms

def test_send_sms():
    dummy_phone = "+1234567890"
    response = send_sms(dummy_phone, "Test notification")
    assert response is not None
