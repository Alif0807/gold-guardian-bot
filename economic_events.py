from forexfactory_service import fetch_calendar

def get_events():

    soup = fetch_calendar()

    if soup is None:
        return []

    # temporary test data
    return [
        {
            "name": "Core CPI m/m",
            "country": "🇺🇸",
            "impact": "🔴",
            "time": "20:30 MYT"
        }
    ]
