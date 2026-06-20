from daily_summary import generate_summary
from telegram_service import send_message

message = generate_summary()

send_message(message)

print("Done")
