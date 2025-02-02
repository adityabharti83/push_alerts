import pytest
from push_alerts import send_email

def test_send_email():
    dummy_email = "test@example.com"
    response = send_email(dummy_email, "Test Subject", "Test notification")
    assert response is None  # No explicit return in send_email
