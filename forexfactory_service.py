import requests
from bs4 import BeautifulSoup

URL = "https://www.forexfactory.com/calendar"

def fetch_calendar():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "lxml")

    return soup
