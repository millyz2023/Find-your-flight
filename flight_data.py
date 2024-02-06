import requests
import datetime
from pprint import pprint
SEARCH_API = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "1GilW-6HoRfauKLSD3UEYzZFIv-muPu-"
SELECTED_CABINS = {
    "economy": "M",
    "economy premium": "W",
    "business": "C",
    "first class": "F",
}
SORT = {
    "price": "price",
    "duration": "duration",
    "quality": "quality",
    "date": "date",
}

# you change the Fly_from & date here
FLY_FROM = "NYC, LAX, CHI, DFW, HOU, WA, PHL, ATL, PHX, SFO, DTT, SAN"
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
    "fly_from": FLY_FROM,
    "fly_to": "",
    "date_from": DATE_FROM,
    "date_to": DATE_TO,
    "selected_cabins": SELECTED_CABINS["business"],
    "curr": "USD",
    "sort": "duration",
    "limit": 100,
}


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data = [
            [
                {
                    "departureLocation1": "",
                    "departureDate1": "",
                    "lowestDuration1": "",
                    "airLines1": "",
                    "ticketPrice1": "",
                }
            ],
            [
                {
                    "departureLocation2": "",
                    "departureDate2": "",
                    "lowestDuration2": "",
                    "airLines2": "",
                    "ticketPrice2": "",
                }
            ],
            [
                {
                    "departureLocation3": "",
                    "departureDate3": "",
                    "lowestDuration3": "",
                    "airLines3": "",
                    "ticketPrice3": "",
                }
            ],
            [
                {
                    "departureLocation4": "",
                    "departureDate4": "",
                    "lowestDuration4": "",
                    "airLines4": "",
                    "ticketPrice4": "",
                }
            ],
        ]

        self.local_data = []


    def search_for_flight(self, fly_to):
        params["fly_to"] = fly_to
        response = requests.get(url=SEARCH_API, headers=header, params=params)
        response.raise_for_status()
        data = response.json()["data"]
        self.local_data = data
        self.clear_data()
        self.add_to_localdata()
        # pprint(data)
    def clear_data(self):
        list = []
        result = []
        for i in self.local_data:
            if i['airlines'] not in list:
                result.append(i)
            list.append(i["airlines"])

        self.local_data = result


    def add_to_localdata(self):
        try:
            for num in range(0, 4):
                airLines = self.local_data[num]['airlines']
                departureLocation = self.local_data[num]['cityFrom']
                departureDate = self.local_data[num]['local_departure']
                lowestDuration = self.local_data[num]['duration']['departure'] / 3600
                ticketPrice = self.local_data[num]['fare']['adults']
                departureDate = departureDate.split("T")[0]
                lowestDuration = round(lowestDuration, 1)
                self.flight_data[num][0][f"departureLocation{num + 1}"] = departureDate
                self.flight_data[num][0][f"departureDate{num + 1}"] = departureLocation
                self.flight_data[num][0][f"lowestDuration{num + 1}"] = lowestDuration
                self.flight_data[num][0][f"airLines{num + 1}"] = airLines
                self.flight_data[num][0][f"ticketPrice{num + 1}"] = ticketPrice

            pprint(self.flight_data)
            return self.flight_data
        except:
            pass

a = FlightData()
a.search_for_flight(fly_to="SYD")


