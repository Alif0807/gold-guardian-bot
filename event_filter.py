HIGH_IMPACT_EVENTS = [
    "Non-Farm Payrolls",
    "Core CPI m/m",
    "CPI m/m",
    "Core PCE Price Index",
    "FOMC Statement",
    "Federal Funds Rate",
    "Powell Speech",
    "Unemployment Claims"
]

def is_high_impact(event_name):
    return any(keyword in event_name for keyword in HIGH_IMPACT_EVENTS)
