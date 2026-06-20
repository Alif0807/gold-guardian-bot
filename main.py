from daily_summary import generate_summary
from scheduler_service import should_send_daily_summary
from telegram_service import send_message

if should_send_daily_summary():

    message = generate_summary()

    send_message(message)

print("Done")
