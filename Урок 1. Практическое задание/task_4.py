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

users = {
    'user_0': {
        'login': 'max',
        'pass': '123',
        'active': True
    },
    'user_1': {
        'login': 'tom',
        'pass': '456',
        'active': True
    },
    'user_2': {
        'login': 'qwe',
        'pass': '789',
        'active': False
    },
    'user_3': {
        'login': 'rty',
        'pass': '012',
        'active': True
    }
}


def auth_0(users, name, password): # O(1)
    if users.get(name):
        if users[name]['pass'] == password and users[name]['active']:        # O(1)
            return 'Пользователь "{name}" авторизован'                       # O(1)
        elif users[name]['pass'] == password and not users[name]['active']:  # O(1)
            return 'Пользователь "{name}" не активен'                        # O(1)
        elif users[name]['pass'] != password:                                # O(1)
            return '"{name}": Неправильный пароль'                           # O(1)
        else:
            return f'Пользователь "{name}" не найден'                        # O(1)


def auth_1 (users, name, password): # O(N)
    for user, status in users.items():                                       # O(N)
        if user == name:                                                     # O(1)
            if status['pass'] == password and status['active']:              # O(1)
                return f'Пользователь "{name}" авторизован'                  # O(1)
            elif status['pass'] == password and not status['active']:        # O(1)
                return f'Пользователь "{name}" не активен'                   # O(1)
            elif status['pass'] != password:                                 # O(1)
                return f'"{name}": Неправильный пароль'                      # O(1)
            else:
                return f'Пользователь "{name}" не найден'                    # O(1)

print(auth_0(users, 'user_0', '123'))
print(auth_0(users, 'user_2', '789'))
print(auth_0(users, 'user_3', '777'))
print(auth_1(users, 'user_0', '123'))
print(auth_1(users, 'user_2', '789'))
print(auth_1(users, 'user_3', '777'))
