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


def authentication(login, password, **users):  # O(N)
    """
    Функция осуществляет проверку пользователя на доступ к ресурсу по соответствию пароля и метки активации
    :param users: dict
        словарь, где ключи - логины, значения - список из пароля [0] и метки активации [1]
    :param login: str
        проверяемый логин
    :param password: str
        проверяемый пароль
    :return: str
        ответ портала о доступе к ресурсу
    """
    for key in users.keys():  # O(N)
        if key == login:
            if users[login][0] == password and users[login][1] == 'active':  # O(1)
                return 'Аутентификация пройдена'  # O(1)
            elif users[login][0] == password and users[login][1] == 'not active':  # O(1)
                return 'Активируйте учётную запись'  # O(1)
            elif users[login][0] != password:  # O(1)
                return 'Пароль неверный'  # O(1)
    return 'Неверный логин' # O(1)

# константная сложность, решение более эффективное, чем перебо всех ключей с каждой проверкой
def authentication_1(login, password, **users):  # O(1)
    if users.get(login):  # O(1)
        if users[login][0] == password and users[login][1] == 'active':  # O(1)
            return 'Аутентификация пройдена'  # O(1)
        elif users[login][0] == password and users[login][1] == 'not active':  # O(1)
            return 'Активируйте учётную запись'  # O(1)
        elif users[login][0] != password:  # O(1)
            return 'Пароль неверный'  # O(1)
    else:
        return 'Неверный логин'


import random

passwords = ['8N2P<O$C', '4*6MGtNM', 'XcFYaPFU', 'LqRYnGg/', 'HIa*Yew4',
             'dpbgivip', 'x7KIn9FL', 'RbI+>Qu4', 'yL6!8j79', 'BB6Ne3r4',
             '5E6lF5bQ', 'nUFb4#Ev', 'nH@I2z-D', 'T9=MsHNZ', '!UWlbj@d',
             'lu+5izB=', '1Ngy9AP+', 'tsU4W@jr', 'SD$#EW0V', '=eP5epJI']
users_names = ['Ivan Boe', 'Petr Coe', 'John Doe', 'Kirill Foe', 'Alex Goe',
               'Tom Hoe', 'Kris Joe', 'Leo Koe', 'Robert Loe', 'Ien Poe',
               'Gregor Toe', 'Martin Soe', 'Mark Roe', 'Tim Xoe', 'Lim Yoe',
               'Tristan Olegovich', 'Tamplier Knight', 'Aluminum tert-butoxide', 'Anyone One', 'Not idea']
activation = [random.choice(['active', 'not active']) for i in range(20)]

users_base = dict(zip(users_names, list(zip(passwords, activation))))
print(users_base)

print(authentication('Ivan Boe', '8N2P<O$C', **users_base))
print(authentication('Martin Soe', '8N2P<O$C', **users_base))
print(authentication('Not idea', '=eP5epJI', **users_base))
