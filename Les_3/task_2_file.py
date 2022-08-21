from hashlib import sha256
import uuid
import csv


def hash_password(password, pepper):
    return sha256(pepper.encode('utf-8') + password.encode('utf-8')).hexdigest()


def check_password(check_pass, user_password, pepper):
    return check_pass == sha256(pepper.encode('utf-8') + user_password.encode('utf-8')).hexdigest()


with open("passwords.csv", "a", newline='') as f:
    first_password = input('Введите пароль: ')
    salt = uuid.uuid4().hex
    hashed_password = hash_password(first_password, salt)
    print('Хэш, отправленный в базу данных: ', hashed_password)
    writer = csv.writer(f)
    writer.writerow([hashed_password, salt])
    second_password = input('Введите пароль еще раз для проверки: ')
    if check_password(hashed_password, second_password, salt):
        print('Вы ввели правильный пароль')
    else:
        print('Пароли не совпадают')
