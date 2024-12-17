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
import os
import json


# Функция для генерации хеша пароля с солью
def generate_password_hash(password, salt=None):
    if salt is None:
        # Генерация случайной соли, если она не передана
        salt = os.urandom(16)

    # Создание хеша с использованием алгоритма SHA-256
    password_hash = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()

    return password_hash, salt


# Функция для сохранения хеша и соли в файл JSON
def save_hash_and_salt(filename: str, password_hash, salt):
    data = {
        "password_hash": password_hash,
        "salt": salt.hex()  # Соль сохраняется в виде строки в шестнадцатеричном формате
    }
    with open(filename, 'w') as file:
        json.dump(data, file)


# Функция для загрузки хеша и соли из файла
def load_hash_and_salt(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    salt = bytes.fromhex(data["salt"])  # Преобразуем соль обратно из строки в байты
    password_hash = data["password_hash"]
    return password_hash, salt


# Основная логика программы
def main():
    filename = "password_data.json"

    # Шаг 1: Запрашиваем пароль и генерируем хеш
    password = input("Введите пароль: ")
    password_hash, salt = generate_password_hash(password)

    # Сохраняем хеш и соль
    save_hash_and_salt(filename, password_hash, salt)

    print(f"В базе данных хранится строка: {password_hash}")

    # Шаг 2: Повторный ввод пароля для проверки
    password_check = input("Введите пароль еще раз для проверки: ")
    password_hash_check, _ = generate_password_hash(password_check, salt)

    # Загружаем сохраненный хеш и соль из файла
    stored_hash, stored_salt = load_hash_and_salt(filename)

    # Проверяем, совпадают ли хеши
    if password_hash_check == stored_hash:
        print("Вы ввели правильный пароль")
    else:
        print("Пароль неверный")


if __name__ == "__main__":
    main()
