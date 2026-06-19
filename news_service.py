import requests
from bs4 import BeautifulSoup

def get_mock_news():
    return {
        "event": "Core CPI m/m",
        "country": "🇺🇸",
        "impact": "🔴 High",
        "time": "20:30 MYT"
    }
