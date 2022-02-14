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


# Общая сложность O(1)
def autorization(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:
            return "Добро пожаловать!"
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:
            return "Учетная запись не активирована, пройдите активацию!"
        elif users[user_name]['password'] != user_password:
            return "Пароль не верный"
    else:
        return "Данного пользователя не существует"


# Общая сложность O(n)
def autorization_a(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать!"
            elif value['password'] == user_password \
                    and not value['activation']:
                return "Учетная запись не активирована, пройдите активацию!"
            elif users['password'] != user_password:
                return "Пароль не верный"
    return "Данного пользователя не существует"
