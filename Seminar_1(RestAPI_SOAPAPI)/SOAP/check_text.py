"""Задание 1
С использованием фреймворка pytest написать тест операции checkText
SOAP API https://speller.yandex.net/services/spellservice?WSDL
Тест должен использовать DDT и проверять наличие определенного
верного слова в списке предложенных исправлений к определенному
неверному слову.
Слова должны быть заданы через фикстуры в conftest.py,
адрес wsdl должен быть вынесен в config.yaml.
Методы работы с SOAP должны быть вынесены в отдельную библиотеку."""

from zeep import Client, Settings
import yaml
with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=data["url"], settings=settings)

# res = client.service.checkText("малоток")
# print(res[0]['s'])
#print(client.service.checkText("малоток"))


def check_text(word):
    return client.service.checkText(word)[0]['s']

#print(check_text('мылоко'))