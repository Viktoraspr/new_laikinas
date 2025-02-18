class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.size = 10

    def run(self):
        print(f'{self.name} run')

    def bark(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f'Our dog {self.name} is barking')


class Cat(Animal):
    def __init__(self, name, age, jump):
        super().__init__(name, age)
        self.jump = jump

    def run(self):
        print(f"Cat {self.name} walk slowly")


dog = Dog('Rikis', 8)
cat = Cat('Muse', 7, True)
print(cat.jump)
print(cat.name)

animal = Animal('Vardas', 10)


our_animals = [dog, cat]
for animal in our_animals:
    animal.run()
    animal.bark()
