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


# 1 сложность o(1)
def authentication_1(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Доступ предоставлен"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Пройдите активацию"
        elif users[user_name]['password'] != user_password:
            return "Пароль не верный"
    else:
        return "Данного пользователя не существует"


# 2 сложность o(n)
def authentication_2(users, user_name, user_password):
    for k, v in users.items():
        if k == user_name:
            if v['password'] == user_password and v['activation']:
                return "Доступ предоставлен"
            elif v['password'] == user_password and not v['activation']:
                return "Пройдите активацию"
            elif v['password'] != user_password:
                return "Пароль не верный"

    return "Данного пользователя не существует"


# Первое решение эффективнее, потому что поиск по ключю имеет сложность о(1), а во втором решении цикл for in


my_users = {'user1': {'password': '111', 'activation': True},
            'user2': {'password': '111', 'activation': True},
            'user3': {'password': '111', 'activation': True},
            'user4': {'password': '111', 'activation': False}
            }

print(authentication_1(my_users, 'user1', '111'))
print(authentication_1(my_users, 'user4', '111'))
print(authentication_1(my_users, 'user1', '1111'))
print(authentication_1(my_users, 'user5', '111'))
print(authentication_1(my_users, 'user1', '111'))
print(authentication_1(my_users, 'user4', '111'))
print(authentication_1(my_users, 'user1', '1111'))
print("*********************************")
print(authentication_2(my_users, 'user1', '111'))
print(authentication_2(my_users, 'user4', '111'))
print(authentication_2(my_users, 'user1', '1111'))
print(authentication_2(my_users, 'user5', '111'))
