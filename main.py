from news_service import get_high_impact_news
from telegram_service import send_message

events = get_high_impact_news()

for event in events:

    message = f"""
🔴 HIGH IMPACT ALERT

{event['country']} {event['event']}

🕒 {event['time']}

⚠️ High volatility expected on XAU/USD.
"""

    send_message(message)

print("Done")
