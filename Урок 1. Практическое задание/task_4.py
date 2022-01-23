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


# Вариант 1 сложность O(n)
def user_login_v1(users, login, password):
    for k, v in users.items():
        if k == login:
            if k == login:
                if v.get('pass') == password:
                    if v.get('activation'):
                        return 'Успешная авторизация'
                    else:
                        return 'Необходимо активировать учётную запись'
                else:
                    return 'Неверный пароль'

    return 'Авторизация не выполнена'


# Вариант 2 сложность O(1)
def user_login_v2(users, login, password):
    user = users.get(login)
    if not user:
        return 'Авторизация не выполнена'
    if user.get('pass') != password:
        return 'Неверный пароль'
    if not user.get('activation'):
        return 'Необходимо активировать учётную запись'
    return 'Успешная авторизация'


if __name__ == '__main__':
    my_users = {'user1': {'pass': 'pass1', 'activation': True}, 'user2': {'pass': 'pass2', 'activation': False},
                'user3': {'pass': 'pass3', 'activation': True}, 'user4': {'pass': 'pass4', 'activation': True},
                'user5': {'pass': 'pass5', 'activation': True}, 'user6': {'pass': 'pass6', 'activation': True}, }
    print(user_login_v1(my_users, '123', '123'))
    print(user_login_v1(my_users, 'user2', 'pass2'))
    print(user_login_v1(my_users, 'user4', '123'))
    print(user_login_v1(my_users, 'user4', 'pass4'))
    print(user_login_v2(my_users, '123', '123'))
    print(user_login_v2(my_users, 'user2', 'pass2'))
    print(user_login_v2(my_users, 'user4', '123'))
    print(user_login_v2(my_users, 'user4', 'pass4'))

"""
    Вариант 2 эффективнее, общая сложность константа, не используется цикл
"""