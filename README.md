# push-alerts

## Overview
`push-alerts` is a Python package that enables sending notifications via multiple channels, including:

- Firebase Push Notifications
- Email (SMTP)
- SMS (Twilio, Nexmo)
- WhatsApp (Twilio API)
- Telegram (Bot API)
- Webhooks (FastAPI)

This package was initially developed as part of my project, **Wheels to Your Doorsteps**, which required a robust notification system. Instead of creating a solution specific to the project, I decided to generalize it into a reusable package for broader use.

🚀 **This package is currently in the publishing process and will be available soon!** Stay tuned for updates.

## Installation
Once available, you will be able to install the package using pip:

```sh
pip install push-alerts
```

## Dependencies
This package relies on the following libraries:

- `firebase-admin` (for Firebase Cloud Messaging)
- `requests` (for HTTP requests)
- `twilio` (for SMS & WhatsApp notifications)
- `smtplib` (for sending emails via SMTP)
- `fastapi` (for webhook support)
- `python-telegram-bot` (for Telegram notifications)
- `python-dotenv` (for environment variable management)

To install dependencies manually, run:
```sh
pip install firebase-admin requests twilio smtplib fastapi python-telegram-bot python-dotenv
```

## Configuration
Set up environment variables (`.env` file) to store your API keys and credentials:

```
FIREBASE_CREDENTIALS=your_firebase_credentials.json
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_email_password
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890
TWILIO_WHATSAPP_NUMBER=whatsapp:+1234567890
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

## Usage
### 1️⃣ Send a Push Notification (Firebase)
```python
from push_alerts import send_push_notification

send_push_notification(
    token="your_device_token",
    title="Hello!",
    body="This is a push notification.",
    data={"key": "value"}
)
```

### 2️⃣ Send an Email
```python
from push_alerts import send_email

send_email("recipient@example.com", "Subject", "Email body content.")
```

### 3️⃣ Send an SMS
```python
from push_alerts import send_sms

send_sms("+1234567890", "This is an SMS notification.")
```

### 4️⃣ Send a WhatsApp Message
```python
from push_alerts import send_whatsapp_message

send_whatsapp_message("+1234567890", "Hello from WhatsApp!")
```

### 5️⃣ Send a Telegram Message
```python
from push_alerts import send_telegram_message

send_telegram_message("your_chat_id", "Hello via Telegram!")
```

### 6️⃣ Webhook Listener (FastAPI)
Run a webhook server to receive notifications:
```python
from push_alerts import webhook_listener
from fastapi import FastAPI

app = FastAPI()
app.include_router(webhook_listener)
```

## Running Tests
Run unit tests using pytest:
```sh
pytest tests/
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
MIT License

