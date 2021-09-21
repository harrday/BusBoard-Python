from datetime import datetime

class Bus:

    def __init__(self, dict):
        self.number = dict['line']
        self.arrival_date = dict['expected']['arrival']['date']
        self.arrival_time = dict['expected']['arrival']['time']
        self.departure_date = dict['expected']['arrival']['date']
        self.departure_time = dict['expected']['arrival']['time']
        self.direction = dict['direction']
        self.minutes = self.minutes_since_midnight(self.arrival_time, self.arrival_date)

    def __str__(self):
        output = f'{self.number:<5} || {self.direction:<20} || {self.arrival_time:<20}'
        return output

    def test(self):
        print('the bus number is ' + self.number)

    def get_minutes(self):
        return self.minutes

    def minutes_since_midnight(self, time, date):
        timehour = int(time[:2])
        timeminute = int(time[3:])
        dateobj = datetime.strptime(date, "%Y-%m-%d")
        currentdatetime = datetime(dateobj.year, dateobj.month, dateobj.day, timehour, timeminute, 0)
        epochdatetime = datetime(1990, 1, 1, 0, 0, 0)
        time_elapsed = (currentdatetime - epochdatetime).total_seconds()//60
        return time_elapsed
