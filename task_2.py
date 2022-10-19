import csv
from hashlib import sha256


def hash():
    salt = sha256('salt'.encode()).hexdigest()
    res = salt + sha256(input('Введите пароль: ').encode()).hexdigest()
    return res


def user():
    user_1 = hash()
    print(f'В базе данных хранится строка: {user_1}')
    with open("users.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([user_1])


def check():
    check_pass = hash()
    with open("users.csv", "r", newline='') as f_1:
        reader = csv.reader(f_1)
        for i in reader:
            if i[0] == check_pass:
                print('Вы ввели правильный пароль')
            else:
                print('Пользователь не найден')


user()
check()
