import datetime
import requests
from pprint import pprint

LOCATIONS_API = "https://api.tequila.kiwi.com/locations/query"
API_KEY = "1GilW-6HoRfauKLSD3UEYzZFIv-muPu-"
SELECTED_CABINS = {
    "economy": "M",
    "economy premium": "W",
    "business": "C",
    "first class": "F",
}

# you change the Fly_from & date here
FLY_FROM = "New York City"
DATE1 = datetime.date.today()
DELTA = datetime.timedelta(days=185)
DATE2 = DATE1 + DELTA
# you change the date here

DATE_FROM = DATE1.strftime("%d/%m/%Y")
DATE_TO = DATE2.strftime("%d/%m/%Y")

header = {
    "apikey": API_KEY
}
params = {
    "term": "",
}


#This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def get_destination_code(self, city):
        params["term"] = city
        response = requests.get(url=LOCATIONS_API, headers=header, params=params)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
