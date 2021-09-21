from datetime import datetime

class Bus:

    def __init__(self, dict):
        self.number = dict['line']
        if dict['expected']['arrival'].get('time') is None or dict['expected']['arrival'].get('date') is None:
            self.arrival_date = dict['date']
            self.arrival_time = dict['aimed_departure_time']
        else:
            self.arrival_date = dict['expected']['arrival']['date']
            self.arrival_time = dict['expected']['arrival']['time']
        if dict['expected']['departure'].get('time') is None or dict['expected']['departure'].get('date') is None:
            self.departure_date = dict['date']
            self.departure_time = dict['aimed_departure_time']
        else:
            self.arrival_date = dict['expected']['departure']['date']
            self.arrival_time = dict['expected']['departure']['time']
        self.direction = dict['direction']
        self.minutes = self.minutes_since_epoch(self.arrival_time, self.arrival_date)

    def __str__(self):
        output = f'{self.number:<5} || {self.direction:<20} || {self.arrival_time:<20}'
        return output

    def get_minutes(self):
        return self.minutes

    def minutes_since_epoch(self, time, date):
        timehour = int(time[:2])
        timeminute = int(time[3:])
        dateobj = datetime.strptime(date, "%Y-%m-%d")
        currentdatetime = datetime(dateobj.year, dateobj.month, dateobj.day, timehour, timeminute, 0)
        epochdatetime = datetime(1990, 1, 1, 0, 0, 0)
        time_elapsed = (currentdatetime - epochdatetime).total_seconds()//60
        return time_elapsed
