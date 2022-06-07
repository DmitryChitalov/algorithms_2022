"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
from uuid import uuid4
import json

data_base = open("log_pas.csv", "w")

us_pas = input('Введите пароль: ') # --> # Az81N
users = {}

userlog = 'Andrey'
password = us_pas

salt = uuid4().hex
pas_key = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
users[userlog] = {
    'userlog': salt,
    'us_pas': pas_key
}

data_base.write(json.dumps(users))
data_base.close()

print(pas_key) # Полученый хеш
with open("log_pas.csv", 'r') as fr:
  base = json.load(fr)
print(base)

re_us_pas = input('Введите пароль еще раз: ')
repeated_password = re_us_pas
salt = users['Andrey']['userlog'] # Получение соли
new_us_pas = users['Andrey']['us_pas'] # Получение правильного ключа
new_pas_key = hashlib.sha256(salt.encode() + re_us_pas.encode()).hexdigest()

if new_pas_key ==pas_key:
  print('Введен правильный пароль')
else:
  print('Неверно введенный пароль.')

  fr.close()