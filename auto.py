from datetime import datetime
from math import ceil


class Driver:
    def drive_safe(self):
        print('This driver drive car very atsargiai')


class Auto:
    pass


class Car(Auto):
    def __init__(self, driver: Driver, new_date: datetime):
        self.driver = driver
        self.date = new_date
        self.seat = 30

    def calculate_busses(self, number=181):
        return ceil(number // 30)

    def do_something(self):
        self.bus_needed()


class Bus(Auto):
    pass


class Truck(Auto):
    pass


