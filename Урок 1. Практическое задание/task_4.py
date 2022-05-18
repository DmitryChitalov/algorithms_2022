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
def check_authorization(users_list: dict, check_username: str) -> bool: # O(N)

    for username, (_, authorized) in users_list.items():  # O(N)
        if username == check_username:  # O(1)
            return authorized  # O(1)


def check_authorization_2(users_list: dict, check_username: str) -> bool: # O(1)

    user = users_list.get(check_username)  # O(1)
    return user[1]  # O(1)


if __name__ == '__main__':
    users = {
        'Alexandr': ('123456', True),
        'Maxim': ('thrw', False),
        'Sascha': ('8764', True),
        'Olga': ('srghtrh', False),
    }

    print(check_authorization(users, 'Alexandr'))
    print(check_authorization(users, 'Maxim'))
    print(check_authorization_2(users, 'Sascha'))
    print(check_authorization_2(users, 'Olga'))
