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

def l3_v2():
    import hashlib
    import json

    data = {}
    name_input = input('Введите имя пользователя')
    hash_input = hashlib.sha256(input('Установите пароль').encode()).hexdigest()
    print(hash_input)
    data[name_input] = hash_input

    with open('passwds.json', 'w', encoding='utf-8') as nf:
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        nf.write(json_str)

    name_compare = input('Имя пользователя')
    hash_compare = hashlib.sha256(input('Пароль').encode()).hexdigest()

    with open('passwds.json', 'r', encoding='utf-8') as nf:
        json_str = nf.read()
        data_set = json.loads(json_str)

    try:
        print(data_set[name_compare] == hash_compare)
        if data_set[name_compare] == hash_compare:
            print('Пароль верный')
        else:
            print('Неверный пароль')
    except KeyError:
        print('Неверное имя пользователя\nПовторный запуск программы\n')
        return l3_v2()


l3_v2()