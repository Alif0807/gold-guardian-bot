import requests
from bs4 import BeautifulSoup

URL = "https://www.forexfactory.com/calendar"

def fetch_calendar():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    print("STATUS:", response.status_code)

    print(response.text[:5000])

    soup = BeautifulSoup(response.text, "lxml")

    return soup
