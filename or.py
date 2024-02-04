import random


class Croissant:
    def __init__(self):
        self.taste = random.randint(50, 100)

    def eat(self, human):
        if human.satiety < 100:
            human.satiety += self.taste
            if human.satiety > 100:
                human.satiety = 100
            print(f"{human.name} насолоджується круасаном!")
        else:
            print(f"{human.name} вже ситий і не може їсти більше.")


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.money = 100

        self.job = job
        self.home = home
        self.car = car

    def get_job(self):
        pass

    def get_home(self):
        pass

    def get_car(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self):
        pass

    def eat_croissant(self, croissant):
        if self.name == "John" and random.choice([True, False]):
            print(f"{self.name} не попався круасан. Він голодний.")
        else:
            croissant.eat(self)


cars = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 8},
    "Opel": {"fuel": 60, "strength": 40, "consumption": 6},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


class Auto:
    def __init__(self, cars):
        self.brand = random.choice(list(cars))
        self.fuel = cars[self.brand]["fuel"]
        self.strength = cars[self.brand]["strength"]
        self.consumption = cars[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Автомобіль не може рухатися")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


nick = Human("Nick")
kate = Human("Kate")
john = Human("John")

croissant = Croissant()

nick.eat_croissant(croissant)
kate.eat_croissant(croissant)
john.eat_croissant(croissant)

доступно
контекстное
меню