import os
import requests
from news_service import get_mock_news

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

news = get_mock_news()

message = f"""
🔴 HIGH IMPACT ALERT

{news['country']} {news['event']}
🕒 {news['time']}

⚠️ High volatility expected on XAU/USD.
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message sent!")
