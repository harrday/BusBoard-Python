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
        number = len(self.departures)
        if number > 5:
            number = 5
        print(f'The next {number} buses to arrive at the stop {self.stop_name} are:')
        i = 0
        while i < number:
            print(self.departures[i])
            i += 1
