"""Задание 2
Написать тест с использованием pytest и requests, в котором:
● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
● conftest.py содержит фикстуру авторизации по адресу
https://test-stand.gb.ru/gateway/login с передачей параметров
“username" и "password" и возвращающей токен авторизации
● Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого
пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts c хедером, содержащим токен
авторизации в параметре "X-Auth-Token". Для отображения
постов другого пользователя передается "owner": "notMe"."""


import requests

responce = requests.post(url="https://test-stand.gb.ru/gateway/login",
                         data={"username": "GB202307c17509",
                               "password": "89578a2581"})
print(responce) # <Response [200]>
print(responce.status_code) # 200
print(responce.json())  # {'id': 20946, 'username': 'GB202307c17509', 'token': 'a69630e0b98652da99efa4d995e7b2f6', 'roles': ['R_STUDENT', 'R_USER', 'P_DUMMY_ACTIVATE', 'P_DUMMY_L', 'P_DUMMY_C', 'P_DUMMY_R', 'P_DUMMY_U', 'P_DUMMY_D', 'P_USER_R', 'P_USER_U', 'P_USER_LOGOUT', 'P_USER_LOGIN']}
print(responce.json()['token'])





