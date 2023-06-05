from django_seed import Seed
from .models import Member
import random


def run():
    seeder = Seed.seeder()
    genders = ['male', 'female']

    seeder.add_entity(Member, 5, {
        "name": lambda x: seeder.faker.name(),
        "age": lambda x: seeder.faker.random.randint(20, 60),
        "gender": lambda x: genders[random.randint(0,1)]
    })

    seeder.execute()
    print("Datas inserted !")