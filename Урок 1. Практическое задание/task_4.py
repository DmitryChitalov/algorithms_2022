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


# Сложность О(1)
def authentication_1(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Ваша учетная запись активирована"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Учетная запись не активирована. Пройдите активацию"
        elif users[user_name]['password'] != user_password:
            return "Неверный пароль"


# Сложность О(n)
def authentication_2(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Ваша учетная запись активирована"
            elif value['password'] == user_password and not value['activation']:
                return "Учетная запись не активирована. Пройдите активацию"
            elif value['password'] != user_password:
                return "Неверный пароль"
    return "Пользователь не найден"


users = {'Антон': {'password': '123', 'activation': True},
         'Анна': {'password': '345', 'activation': True},
         'Борис': {'password': '567', 'activation': True},
         'Евгений': {'password': '789', 'activation': False}
         }

print(authentication_1(users, 'Антон', '123'))
print(authentication_1(users, 'Евгений', '789'))
print(authentication_1(users, 'Анна', '789'))
print(authentication_2(users, 'Антон', '123'))
print(authentication_2(users, 'Евгений', '789'))
print(authentication_2(users, 'Анна', '789'))

# Первое решение будет более быстрым , и выглядит более локонично
