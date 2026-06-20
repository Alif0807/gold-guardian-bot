from economic_events import get_events
from telegram_service import send_message

events = get_events()

for event in events:

    message = f"""
{event['impact']} HIGH IMPACT ALERT

{event['country']} {event['name']}

🕒 {event['time']}

⚠️ XAU/USD volatility expected.
"""

    send_message(message)

print("Done")
