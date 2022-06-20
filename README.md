# Online-Employee-Directory-DRF
Скачиваем проект через

git clone https://github.com/YerkebulanYO/Online-Employee-Directory-DRF.git

переходим в папку Online-Employee-Directory-DRF в терминале

пишем команду python3 manage.py runserver или python manage.py runserver

переходим в ссылку http://127.0.0.1:8000/api/v1/employees/

Пройдите аутентификацию 
login: AccountToCheck1

password: 13579_Q1

Сортировку можно произвести через ordering например:

http://127.0.0.1:8000/api/v1/employees/?ordering=id

Фильтр:

http://127.0.0.1:8000/api/v1/employees/?position=Intern
