import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employeeProject.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()

from base.models import Employee


def all_employees_info():
    Employee.objects.all()

def searching_employee():
    pass

def sorting_employees():
    pass

def register():
    pass

def crud():
    pass

def main():
    while True:
        print('Привет, какую команду хотите использовать? \n')
        print('\n')
        print('Печатай 1 если хотите чтобы вывело список всех сотрудников со всей инфой о сотруднике (Опциональная часть: пункт 3)\n')
        print('Печатай 2 если хочешь произвести поиск сотрудника через поле (Опциональная часть: пункт 4)\n')
        print('Печатай 3 если хочешь сортировать (Опциональная часть: пункт 5)\n')
        print('Печатай 4 если хочешь зарегистрироваться() \n')
        print('Печатай 5 если хочешь CRUD на данных сотрудников\n')

        request = int(input('Сан жаз: '))

        if request == 1:
            all_employees_info()
        elif request == 2:
            searching_employee()
        elif request == 3:
            sorting_employees()
        elif request == 4:
            register()
        elif request == 5:
            crud()
        else:
            print('Не то число напечатал')



if __name__ == '__main__':
    main()
