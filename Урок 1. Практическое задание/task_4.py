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


def auth_checker_v1(log, passwd, data):  # Сложность - O(1)
    try:
        if data[log][0] == passwd and data[log][1]:
            answer = 'Ok'
        else:
            answer = 'Account not activated'
    except KeyError:
        answer = 'Wrong log or password'
    return answer


def auth_checker_v2(log, passwd, data):  # Сложность - O(n):
    if log in data.keys() and passwd in data[log]:  # n + 1
        if data[log][1]:
            answer = 'Ok'
        else:
            answer = 'Account not activated'
    else:
        answer = 'Wrong log or password'
    return answer


if __name__ == '__main__':
    profile_data = {
        'login_1': ['passwd_1', 1],
        'login_2': ['passwd_2', 0],
        'login_3': ['passwd_3', 0],
        'login_4': ['passwd_4', 0],
        'login_5': ['passwd_5', 1],
        'login_6': ['passwd_6', 1]
    }
    print('Попытка авторизации с помощью функции v1:')
    print('_' * 50)
    for num in range(0, 8):
        login = f'login_{num}'
        password = f'passwd_{num}'
        print(auth_checker_v1(login, password, profile_data))

    print('\nПопытка авторизации с помощью функции v2:')
    print('_' * 50)
    for num in range(0, 8):
        login = f'login_{num}'
        password = f'passwd_{num}'
        print(auth_checker_v2(login, password, profile_data))

'Первое решение более удачное, т.к. не требует проверки на вхождение, а использует try:except'
