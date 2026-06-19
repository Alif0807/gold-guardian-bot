import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """
🔥 GOLD GUARDIAN ONLINE 🔥

Hello bro 😎

Your Gold Guardian AI is now running on GitHub Actions.

Next upgrades:
🔴 High-impact news alerts
📈 XAUUSD technical alerts
🤖 AI analysis
📅 Daily summaries

Stay tuned 🚀
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Telegram message sent successfully!")
