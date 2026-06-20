from economic_events import get_events

def generate_summary():

    events = get_events()

    message = "📅 TODAY'S HIGH IMPACT EVENTS\n\n"

    for event in events:

        message += (
            f"{event['impact']} "
            f"{event['country']} "
            f"{event['name']}\n"
            f"🕒 {event['time']}\n\n"
        )

    return message
