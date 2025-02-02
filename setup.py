from setuptools import setup, find_packages

setup(
    name="push-alerts",
    version="0.1.0",
    description="A Python package for multi-channel notifications",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "firebase-admin",
        "requests",
        "twilio",
        "smtplib",
        "fastapi",
        "python-telegram-bot",
        "python-dotenv"
    ],
)
