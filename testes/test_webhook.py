import pytest
from fastapi.testclient import TestClient
from push_alerts.webhook import webhook_listener
from fastapi import FastAPI

app = FastAPI()
app.include_router(webhook_listener)
client = TestClient(app)

def test_webhook_listener():
    response = client.post("/webhook", json={"event": "test", "message": "Test webhook"})
    assert response.status_code == 200
    assert response.json() == {"status": "received"}
