
class Auto:
    def __init__(self, tyres: int = 4, color: str = 'blue', kablys: bool = True, **kwargs):
        self.tyres = tyres
        self.color = color
        self.is_kablys = kablys
        self.ratai: int = kwargs.get('varomi_ratai', 2)
        self.a = None
        self.my_data = list(range(1, 50))

    def __str__(self):
        return f'Automobilis, kurio spalva yra {self.color}. Str metodas'

    def __repr__(self):
        return f'Automobilis, kurio spalva yra {self.color}. Spausdina repr metoda'

    def __len__(self):
        return len(self.my_data)

    def run_to(self, address: str):
        print(f'Our car is {self.color} and is running to {address}')

    def lift_somebody(self, address: str, person: str = 'Jonas'):
        my_address = address
        print(f'Take {person}')
        self.run_to(address=my_address)

    def set_tyres(self, tyres: int):
        self.tyres = tyres


class Bus:
    def __init__(self, color='blue'):
        self.color = color

    def run_to(self, address: str):
        print(f'Our car is {self.color} and is running to {address}')


def run(address_pizzas: str = 'Pasilaiciu20', address_passengers: str = 'Klaipeda'):
    auto = Auto()
    bus = Bus()

    auto.run_to(address=address_pizzas)
    bus.run_to(address=address_passengers)


class Human:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def open_file(self):
        print(self.path_to_file)

    def read(self):
        self.open_file()
        pass

    def write(self):
        self.open_file()
        # open file
        pass

    def run(self):
        pass


auto = Auto(tyres=4)
auto_2 = Auto(color='red')
# print(auto.tyres)
# auto.set_tyres(5)
# auto.tyres = 5
# print(auto.tyres)

print(auto)
print(auto_2)
print([auto, auto_2])

print(len(auto))
print(auto.__len__())
