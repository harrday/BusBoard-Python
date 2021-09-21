import requests
from busstop import BusStop
from nearbystops import *
from constants import APPDETAILS

key = APPDETAILS


def main():
    print("Welcome to BusBoard.")

    postcode = input('Please enter your postcode:')


    select = ''
    while select != '1' and select != '2':
        select = input('Do you want to view: \n'
                       '1: The 5 closest bus stops to your location \n'
                       '2: The 5 soonest buses at your 2 closest bus stops')
        if select == '1':
            nearbystops(postcode)
        elif select == '2':
            closesttwo(postcode)
            print(f'Your closest stops are: ')

        else:
            pass


if __name__ == "__main__":
    main()
