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


def check_auth1(user_dict: dict, login: str, password: str):
    """O(n)"""
    for user_login, user_params in user_dict.items():  # O(n)
        if user_login == login and user_params.get('password') == password:  # O(1)
            if user_params.get('is_active'):  # O(1)
                return 'OK'  # O(1)
            else:
                return 'Activation required'  # O(1)
    return 'Incorrect login/password'  # O(1)


def check_auth2(user_dict: dict, login: str, password: str):
    """ O(1)"""
    user_data = user_dict.get(login)  # O(1)
    if user_data:
        if user_data.get('password') == password:  # O(1)
            if user_data.get('is_active'):  # O(1)
                return 'OK'  # O(1)
            else:
                return 'Activation required'  # O(1)
    return 'Incorrect login/password'  # O(1)


if __name__ == '__main__':
    userdict = {'user' + str(i): {'password': 'fdfd', 'is_active': bool(i % 2)}
                for i in range(15)}
    print(userdict)
    print(check_auth1(userdict, 'user1', 'fdfd'))
    print(check_auth1(userdict, 'user1t', 'fdfd'))
    print(check_auth1(userdict, 'user1', 'fdf'))
    print(check_auth1(userdict, 'user2', 'fdfd'))
    print(check_auth2(userdict, 'user1', 'fdfd'))
    print(check_auth2(userdict, 'user2', 'fdfd'))

# Второй вариант лучше, т.к. доступ к словарю по ключу эффективнее перебора
