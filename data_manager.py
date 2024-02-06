import requests
from pprint import pprint

SHEETY_API_URLS = "https://api.sheety.co/3b55d1c3a4a596338fa57f0fd6d4c919/worksFlightPlans/prices"
SHEETY_PUT_URLS = "https://api.sheety.co/3b55d1c3a4a596338fa57f0fd6d4c919/worksFlightPlans/prices"
AUTHORIZATION = "Basic bWVpbGluZ3poYW86SnVuZVBhcmlzIzEx"
header = {
    'Authorization': AUTHORIZATION
}

#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_URLS, headers=header)
        response.raise_for_status()
        data = response.json()["prices"]
        self.destination_data = data
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f'{SHEETY_PUT_URLS}/{city["id"]}',
                json=new_data
            )

            print(response.text)

    def write_research(self, data_base, id):
        new_data = {
            "price": {
                "airLines1": data_base[0][0]['airLines1'],
                "departureDate1": data_base[0][0]["departureDate1"],
                "departureLocation1": data_base[0][0]["departureLocation1"],
                "lowestDuration1": data_base[0][0]["lowestDuration1"],
                "ticketPrice1": data_base[0][0]["ticketPrice1"],
                "airLines2": data_base[1][0]['airLines2'],
                "departureDate2": data_base[1][0]["departureDate2"],
                "departureLocation2": data_base[1][0]["departureLocation2"],
                "lowestDuration2": data_base[1][0]["lowestDuration2"],
                "ticketPrice2": data_base[1][0]["ticketPrice2"],
                "airLines3": data_base[2][0]['airLines3'],
                "departureDate3": data_base[2][0]["departureDate3"],
                "departureLocation3": data_base[2][0]["departureLocation3"],
                "lowestDuration3": data_base[2][0]["lowestDuration3"],
                "ticketPrice3": data_base[2][0]["ticketPrice3"],
                "airLines4": data_base[3][0]['airLines4'],
                "departureDate4": data_base[3][0]["departureDate4"],
                "departureLocation4": data_base[3][0]["departureLocation4"],
                "lowestDuration4": data_base[3][0]["lowestDuration4"],
                "ticketPrice4": data_base[3][0]["ticketPrice4"],

            }
        }

        response = requests.put(
            url=f'{SHEETY_PUT_URLS}/{id}',
            json=new_data
        )
        print("succeed in writing")

