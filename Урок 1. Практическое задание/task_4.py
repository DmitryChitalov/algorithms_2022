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


storage = [
    {'login': 'user_1', 'password': '1234', 'activation': False},
    {'login': 'user_2', 'password': '4321', 'activation': True},
    {'login': 'user_3', 'password': '0000', 'activation': False}
]


def authentication_1(login, password):
    """ Сложность: O(n) """
    for idx, account in enumerate(storage):
        if account['login'] == login and account['password'] == password:
            if not account['activation']:
                if input(f'{login}, your account is not activated, activate now? (y/n) ') == 'y':
                    storage[idx]['activation'] = True
                else:
                    return False
            return True
    return False


def authentication_2(login, password):
    """ Сложность: O(n^2) """
    for account in storage:
        if account['login'] == login and account['password'] == password:
            if not account['activation']:
                if input(f'{login}, your account is not activated, activate now? (y/n) ') == 'y':
                    idx = 0
                    for acc in storage:
                        if acc['login'] == login:
                            storage[idx]['activation'] = True
                        else:
                            idx += 1
                else:
                    return False
            return True
    return False


print(authentication_1('user_1', '1234'))
print(authentication_1('user_2', '4321'))
print(authentication_1('user_3', '5453'))

print()

print(authentication_2('user_1', '1234'))
print(authentication_2('user_2', '4321'))
print(authentication_2('user_3', '5453'))
