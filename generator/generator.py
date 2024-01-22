import random

from data.data import Person
from faker import Faker


faker = Faker()


def generated_person():
    return Person(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        current_address=faker.address(),
        mobile=faker.msisdn(),
        subject="English"
    )


def generated_file():
    path = r"f:\LocalRepository\AQA_Python\upload_file.txt"
    file = open(path, "w")
    file.write(f"Helloworld{random.randint(23, 100)}")
    file.close()
    return path
