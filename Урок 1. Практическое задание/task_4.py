"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from itertools import islice

users = {'John': {'login': 'qwerty', 'password': '4k9i', 'is_authenticated': 0},
         'Stone': {'login': 'qwy', 'password': '4529i', 'is_authenticated': 1},
         'Andrey': {'login': 'swe', 'password': '123456', 'is_authenticated': 1},
         'Weirdo': {'login': 'ty', 'password': '12345', 'is_authenticated': 0},
         'Sasha': {'login': 'asd', 'password': '1234', 'is_authenticated': 0},
         'Alexey': {'login': 'zxc', 'password': '123', 'is_authenticated': 1}}


def check_authentication(key):  # Итог: O(n)
    for v in islice(key.values(), 2, 3):  # O(n)
        if v == 0:  # O(n)
            print('We suggest you to complete authentication')  # O(1)
        else:
            print('All right')  # O(1)


check_authentication(users['Weirdo'])
check_authentication(users['Alexey'])


def check_authentication_v2(key):  # Итог: O(n^2)
    for i in key.items():  # O(n^2)
        for v in i:  # O(n)
            if v == 0:  # O(n)
                print('We suggest you to complete authentication')  # O(1)
            elif v == 1:  # O(n)
                print('All right')  # O(1)


check_authentication(users['Weirdo'])
check_authentication(users['Alexey'])
