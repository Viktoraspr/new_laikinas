class Driver:
    def drive_safe(self):
        print('This driver drive car very atsargiai')


class Auto:
    pass


class Car(Auto):
    def __init__(self, driver: Driver):
        self.driver = driver

    def do_something(self):
        self.driver.drive_safe()


class Bus(Auto):
    pass


class Truck(Auto):
    pass


driver = Driver()
car = Car(driver=driver)
