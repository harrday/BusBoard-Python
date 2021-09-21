import requests
from busdata import Bus
from busstop import BusStop

def main():
    print("Welcome to BusBoard.")
    r = requests.get(f'http://transportapi.com/v3/uk/bus/stop/490000077E/live.json?app_id=7959bd3c&app_key=4ff4429381da12abe16b36e2cc951f69')
    response = r.json()

    b = BusStop(response)
    b.giveDepartures()

if __name__ == "__main__":
    main()