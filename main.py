from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
SHEETY_PUT_URLS = "https://api.sheety.co/3b55d1c3a4a596338fa57f0fd6d4c919/worksFlightPlans/prices/"
# print(sheet_data)
flight_search_helper = FlightData()

for items in sheet_data:
    if items["iataCode"] == '':
        from flightcode_search import FlightSearch
        flight_code_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_code_search.get_destination_code(row["city"])

        data_manager.destination_data = sheet_data
        data_manager.update_destination_data()

for item in sheet_data:
    flight_search_helper.search_for_flight(fly_to=item["iataCode"])
    database = flight_search_helper.flight_data
    print(f"{item['city']},{database}")

