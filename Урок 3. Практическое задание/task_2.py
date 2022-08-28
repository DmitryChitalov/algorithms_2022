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
salt = 'my_salt'
paswd = input('Введите пароль: ')
paswd_2 = input('Повторите пароль: ')
hesh_1 = hashlib.sha256(paswd.encode() + salt.encode()).hexdigest()
hesh_2 = hashlib.sha256(paswd_2.encode() + salt.encode()).hexdigest()


def checer(first, second):
    if first == second:
        return f'Пароль верный'
    else:
        return f'Пароли не совпадают'


print(hesh_1, hesh_2)
print(checer(hesh_1, hesh_2))