import requests
from constants import APPDETAILS
from singlestop import SingleStop
from busstop import BusStop

key = APPDETAILS

class NearbyStops:

    def __init__(self, dict):
        self.stops = []

        for busstop in dict:
            singlestop = SingleStop(busstop)
            self.stops.append(singlestop)

    def giveStops(self):
        print(f'The 5 closest stops to your location are')
        i = 0
        while i < 5:
            print(self.stops[i])
            i += 1

    def giveStopsAndBuses(self):
        for i in range(len(self.stops)):
            atcocode = self.stops[i].atcocode
            r = requests.get(f'http://transportapi.com/v3/uk/bus/stop/{atcocode}/live.json?app_id={key["app_id"]}'
                             f'&app_key={key["app_key"]}')
            response = r.json()
            b = BusStop(response)
            b.giveDepartures()


def pctoll(postcode):  # converts postcode to longitude and latitude
    pc = requests.get(f'https://api.postcodes.io/postcodes?q={postcode}')
    response = pc.json()
    longitude = response['result'][0]['longitude']
    latitude = response['result'][0]['latitude']
    coords = [longitude, latitude]
    return coords


def nearbystops(postcode):  # gives 5 closest stops and distances from postcode
    coords = pctoll(postcode)
    near = requests.get(f'https://transportapi.com/v3/uk/places.json?lat={coords[1]}&lon={coords[0]}'
                        f'&type=bus_stop&app_id={key["app_id"]}&app_key={key["app_key"]}')
    response = near.json()
    t = NearbyStops(response['member'])
    return t.giveStops()

def closesttwo(postcode):  # gives 2 closest stops and bus times from postcode
    coords = pctoll(postcode)
    near = requests.get(f'https://transportapi.com/v3/uk/places.json?lat={coords[1]}&lon={coords[0]}'
                        f'&type=bus_stop&app_id={key["app_id"]}&app_key={key["app_key"]}')
    response = near.json()
    closest = response['member'][0:2]
    t = NearbyStops(closest)
    return t.giveStopsAndBuses()