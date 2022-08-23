"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

import csv


# Как я понимаю задание, мы моделируем ситуацию, когда какой-то юзер пытается зайти на сайт
# и мы проверяем, верный ли у него логин и пароль, помимо активации. Файл users.csv имитирует
# базу данных и имеет формат строки никнейм,пароль,активация в виде 1 или 0 как True или False.
def autentification():  # O(n)
    with open('users.csv', 'r') as file:  # O(1)
        users = list(csv.reader(file))  # O(1) ???
        login_auth = input('Введите Ваш никнейм: ')  # O(1)
        password_auth = input('Введите Ваш пароль: ')  # O(1)
        user_list = []  # O(1)
        password_list = []  # O(1)
        activation_list = []  # O(1)
        for row in users:  # O(n)
            user_list.append(row[0])  # O(1)
            password_list.append(row[1])  # O(1)
            activation_list.append(row[2])  # O(1)
        if login_auth in user_list:  # O(n)
            if password_auth == password_list[user_list.index(login_auth)]:  # O(1)
                if int(activation_list[user_list.index(login_auth)]):  # O(1)
                    print('Добро пожаловать, ' + login_auth + '!')  # O(1)
                else:
                    print(login_auth + ', Вам необходимо активировать аккаунт!')  # O(1)
            else:
                print('Неверный пароль!')  # O(1)
        else:
            print('Пользователя нет в базе данных!')  # O(1)


autentification()
# Второй способ с реализацией БД через словарь.
user_db = {'user1': ['blahblah', True], 'user2': ['blahblah', False], 'user3': ['blahblah', True],
           'user4': ['blahblah', True], }


def autentification_2(users, user_name, password):  # O(1)
    if users.get(user_name):  # O(1)
        if users[user_name][0] == password:  # O(1)
            if users[user_name][1]:  # O(1)
                return f'Добро пожаловать, {user_name}! Авторизация выполнена успешно.'  # O(1)
            else:  # O(1)
                return f'{user_name}, Вам необходимо активировать аккаунт!'  # O(1)
        else:  # O(1)
            return 'Неверный пароль!'  # O(1)
    else:  # O(1)
        return f'Пользователя с ником {user_name} не существует!'  # O(1)


print(autentification_2(user_db, 'user3', 'blahblah'))
print(autentification_2(user_db, 'user2', 'blahblah'))
print(autentification_2(user_db, 'user1', 'halbhalb'))
print(autentification_2(user_db, 'user6', 'blahblah'))
