class SingleStop:

    def __init__(self, dict):
        self.atcocode = dict['atcocode']
        self.stop_name = dict['name']
        self.distance = dict['distance']

    def __str__(self):
        output = f'{self.stop_name:<25} || {int(self.distance)}m'
        return output
