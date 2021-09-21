from busdata import *

class BusStop:

    def __init__(self, dict):
        self.atcocode = dict['atcocode']
        self.smscode = dict['smscode']
        self.stop_name = dict['stop_name']
        self.name = dict['name']
        self.locality = dict['locality']
        self.departures = []

        for bus_number in dict['departures']:
            for specific_bus in dict['departures'][bus_number]:
                bus_class = Bus(specific_bus)
                self.departures.append(bus_class)

    def sortDepartures(self):
        self.departures.sort(key=lambda bus: bus.get_minutes())

    def giveDepartures(self):
        self.sortDepartures()
        print(f'The next 5 buses to arrive at this stop ({self.stop_name}) are:')
        i = 0
        while i < 5 and self.departures[i] is not None:
            print(self.departures[i])
            i += 1
