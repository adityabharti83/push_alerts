import pytest
from push_alerts import send_push_notification

def test_send_push_notification():
    dummy_token = "dummy_device_token"
    response = send_push_notification(dummy_token, "Test Title", "Test notification")
    assert response is not None
