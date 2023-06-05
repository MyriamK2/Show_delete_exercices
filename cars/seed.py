from django_seed import Seed
from .models import Car
import random

def run():
    seeder = Seed.seeder()

    seeder.add_entity(Car, 25, {
        "brand": lambda x: seeder.faker.word(ext_word_list=["Ford", "BMW", "Mercedes", "Citroen", "Peugeot", "Toyota", "Jeep", "Porsche", "Lamborghini", "Ferrari"]),
        "year": lambda x: seeder.faker.year(),
        "color": lambda x: seeder.faker.color_name(),
        "price": lambda x: random.randint(3000,10000),
        "discount": lambda x: seeder.faker.pyint(min_value=20, max_value=70, step=5)
    })

    seeder.execute()
    print("Into cars_car !")