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
users = {
    'dmitriy': ['123456', 'Activated'],
    'ivan': ['654321', 'Not activated'],
    'lena': ['111111', 'Activated']
}

def authorization_1(users, username, password):  # O(1)
    if username in users.keys():
        if password == users[username][0] and users[username][1] == 'Activated':
            return 'Поздравляем, вы допущены к веб-ресурсу!'
        elif password == users[username][0] and users[username][1] == 'Not activated':
            return 'Вам нужно активировать свою учетную запись.'
        elif password != users[username][0]:
            return 'Неправильный пароль.'
    else:
        return f'Пользователь с логином {username} не найден.'

def authorization_2(users, username, password):  # O(n)
    for key, value in users.items():
        if key == username:
            if password == value[0] and value[1] == 'Activated':
                return 'Поздравляем, вы допущены к веб-ресурсу!'
            elif password == value[0] and value[1] == 'Not activated':
                return 'Вам нужно активировать свою учетную запись.'
            elif password != value[0]:
                return 'Неправильный пароль.'
    return f'Пользователь с логином {username} не найден.'

print(authorization_1(users, 'babai', '111111'))
print(authorization_2(users, 'ivan', '654321'))