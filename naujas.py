from datetime import datetime


class Driver:
    def __init__(self,
                 vacation_date: datetime,
                 categories_present: int = {"B"},
                 charge_for_km: float = 6.35,
                 fullname: str = "Ratenis Vairavičius",
                 binging_issues: bool = False):
        self.vacation_date = vacation_date
        self.categories_present = categories_present
        self.charge_for_km = charge_for_km
        self.fullname = fullname
        self.binging_issues = binging_issues


class Vehicle:
    def __init__(self,
                 annual_mileage: int = 0,
                 license_plate: str = "",
                 fuel_type: str = "gasoline",
                 fuel_consumption: int = 5,
                 fixed_costs: int = 0,
                 inspection_date = "",
                 driver_category_required: set = {"B"},
                 ):
        print("Run")
        self.annual_mileage = annual_mileage
        self.license_plate = license_plate
        self.fuel_type = fuel_type
        self.fixed_costs = fixed_costs
        self.inspection_date = inspection_date
        self.driver_category_required= driver_category_required
        self.fuel_consumption = fuel_consumption

    def if_technical_inspection_soon(self):
        pass

    def calculate_cost_per_km(self):

        if self.fuel_type == "gasoline" or "petrol":
            fuel_cost = 5
        elif self.fuel_type == "diesel":
            fuel_cost = 4
        elif self.fuel_type == "electric":
            fuel_cost = 3
        else:
            fuel_cost = 1

        cost_per_km = self.fixed_costs + self.annual_mileage * self.fuel_consumption/100 * fuel_cost
        return cost_per_km


class Car(Vehicle):
    def __init__(self, annual_mileage: int = 0, license_plate: str = "", fuel_type: str = "gasoline",
                 fuel_consumption: int = 5, fixed_costs: int = 0, inspection_date="",
                 driver_category_required: set = {"B"}):
        super().__init__()
        print("Fast run")


class Bus(Vehicle):
    def __init__(self,
                 seating_capacity: int = 15
                 ):
        super().__init__()
        print("Yellow run")
        self.seating_capacity = seating_capacity


    def calculate_bus_for_n_passengers(self):
        pass

    def calculate_estimate_cost(self):
        pass


class Truck(Vehicle):
    def __init__(self,
                 cargo_capacity: int = 1000,
                 wagon_option: bool = False,
                 wagon_capacity: int = 0,
                 ):
        super().__init__()
        print("Loaded run")
        self.cargo_capacity = cargo_capacity
        self.wagon_option = wagon_option
        self.wagon_capacity = wagon_capacity


car = Car(
    annual_mileage=1,
    fuel_type="petrol",
    fuel_consumption=5,
    fixed_costs=0,
    inspection_date="",
    driver_category_required={"B"},
)
