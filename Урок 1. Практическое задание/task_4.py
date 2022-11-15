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


def is_granted_1(accounts: dict, login: str, passw: str) -> str:  # O(n)
    for key, val in accounts.items():
        if login == key:
            if passw == val[0]:
                if val[1] == 'activated':
                    return f'{key}, добро пожаловать'
                else:
                    return f'{key}, пройдите активацию'
    return f'Пожалуйста, проверьте логин и пароль, или зарегистрируйтесь'


def is_granted_2(accounts: dict, login: str, passw: str) -> str:  # O(1)
    if accounts.get(login) is None or accounts.get(login)[0] != passw:
        return f'Пожалуйста, проверьте логин и пароль, или зарегистрируйтесь'
    else:
        if not accounts.get(login)[1] == 'activated':
            return f'{login}, пройдите активацию'
        else:
            return f'{login}, добро пожаловать'


user_accounts = {
    'ivan': ('1234', 'not activated'),
    'egor': ('6487', 'activated'),
    'grigorij': ('7381', 'not activated')
}

print('\n')
print(is_granted_1(user_accounts, 'egor', '6487'))
print(is_granted_1(user_accounts, 'grigorij33', '6488'))
print(is_granted_1(user_accounts, 'ivan', '1234'))
print('\n')
print(is_granted_2(user_accounts, 'egor', '6487'))
print(is_granted_2(user_accounts, 'grigorij33', '6488'))
print(is_granted_2(user_accounts, 'ivan', '1234'))
