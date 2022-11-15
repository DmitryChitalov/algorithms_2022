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


def auth(users):  # O(1)
    login = input('Login: ')
    password = input('Password: ')
    try:
        selected_user = users[login]
    except:
        return 'Wrong user'
    if password != selected_user['pass']:
        return 'Wrong password'
    return 'Access granted' if selected_user['active'] else 'Please activate account'


def auth_for(users):  # O(n)
    login = input('Login: ')
    password = input('Password: ')
    for key, body in users.items():  # O(n)
        if key == login:
            if password != body['pass']:
                return 'Wrong password'
            return 'Access granted' if body['active'] else 'Please activate account'

    return 'Wrong user'


usersList = {
    'user1': {'pass': 'pass1', 'active': True},
    'user2': {'pass': 'pass2', 'active': False},
    'user3': {'pass': 'pass1', 'active': True},
}

print(auth(usersList))
print(auth_for(usersList))
