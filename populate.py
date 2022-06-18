import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employeeProject.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()

import random
from base.models import Employee
from faker import Faker
import datetime

fake = Faker()

POS = [
    'Intern',
    'Junior',
    'Middle',
    'Senior',
    'President'
]

def create_date():
    start_date = datetime.date(2014, 1, 1)
    end_date = datetime.date(2022, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def populate(value):
    first_personal()

    for i in range(value):
        name = fake.name()
        pos = random.choice(POS)

        date = create_date()
        salary = fake.random_int(min=10000, max=500000)

        head = ''
        print(pos)

        if pos == 'Intern':
            head = 'Junior'
        elif pos == 'Junior':
            head = 'Middle'
        elif pos == 'Middle':
            head = 'Senior'
        elif pos == 'Senior':
            head = 'President'
        else:
            head = None


        if pos != 'President':
            all_bastyq = Employee.objects.filter(position=head)
            bastyq = random.choice(all_bastyq)
        else:
            bastyq = None

        Employee.objects.create(
            full_name=name,
            position=pos,
            employment_date=date,
            salary=salary,
            boss=bastyq
        )


def first_personal():
    president = Employee.objects.create(full_name=fake.name(), position='President', employment_date=create_date(), salary=fake.random_int(min=10000, max=500000), boss=None)
    senior = Employee.objects.create(full_name=fake.name(), position='Senior', employment_date=create_date(), salary=fake.random_int(min=10000, max=500000), boss=president)
    middle = Employee.objects.create(full_name=fake.name(), position='Middle', employment_date=create_date(), salary=fake.random_int(min=10000, max=500000), boss=senior)
    junior = Employee.objects.create(full_name=fake.name(), position='Junior', employment_date=create_date(), salary=fake.random_int(min=10000, max=500000), boss=middle)
    intern = Employee.objects.create(full_name=fake.name(), position='Intern', employment_date=create_date(), salary=fake.random_int(min=10000, max=500000), boss=junior)


def main():
    v = int(input('Number of workers: '))
    populate(v)

if __name__ == '__main__':
    main()
