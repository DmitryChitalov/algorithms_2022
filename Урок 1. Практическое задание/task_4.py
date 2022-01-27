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

# Решение №1
# Сложность O(n)

users = {'ivanov': ('password1', 0), 'petrov': ('password2', 1), 'sidorov': ('password3', 0)}


def auth_func(user_login, user_password):
    for key, val in users.items():  # O(n)
        if user_login == key and user_password == val[0]:  # O(1)
            if val[1] == 0:  # O(1)
                print('Your account is inactive. Do you want to activate it? (Y/N)')  # O(1)
                if input().lower() == 'y':  # O(1)
                    users[key] = (user_password, 1)  # O(1)
                    return print("Activated. Access granted")  # O(1)
            else:
                return print("Access granted")  # O(1)
    return print('Access denied')  # O(1)


# auth_func('ivanov', 'password1')


# Решение №2
# Сложность O(1)


users = {'ivanov': ('password1', 0), 'petrov': ('password2', 1), 'sidorov': ('password3', 0)}


def auth_func(user_login, user_password):
    if users.get(user_login) and user_password == users.get(user_login)[0]:  # O(1)
        if users.get(user_login)[1] == 0:  # O(1)
            print('Your account is inactive. Do you want to activate it? (Y/N)')  # O(1)
            if input().lower() == 'y':  # O(1)
                users[user_login] = (user_password, 1)  # O(1)
                return print("Activated. Access granted")  # O(1)
        else:
            return print("Access granted")  # O(1)
    return print('Access denied')  # O(1)


auth_func('ivanov', 'password1')