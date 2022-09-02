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
import hashlib, csv


def create_hash_password():
    login = input("Enter login: ")
    password = input("Enter password: ")
    hash_password = set()
    hash_password = hashlib.sha256(password.encode("utf-8") + login.encode("utf-8")).hexdigest()
    print(f'Хэш + соль = {hash_password}, Логин = {login}, Пароль = {password}')
    return hash_password


def write_hash_password(hash_password):
    start_exit = input("Введите любую клавишу для начала или 0 для выхода: ")
    if start_exit == '0':
        print("Выход")
    else:
        print(f'Хэш + соль = {hash_password}')
        with open('data.csv', 'r+') as file:
            file.write(hash_password)
            file.write("\n")
            for line in file:
                if hash_password in line:
                    print("Совпадение найдено")
                else:
                    print("Ваши данные занесены в базу")
        return write_hash_password(hash_password)


if __name__ == "__main__":
    write_hash_password(create_hash_password())

