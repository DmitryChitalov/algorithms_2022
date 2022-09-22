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


# общая сложность O(n)
def authorization_1(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return (f'Пользователь {user_name} допущен к ресурсу.')
            elif value['password'] == user_password \
                    and not value['activation']:
                return (f'Пользователь {user_name} не допущен к ресурсу. Необходимо пройти аутентификацию.')
            elif value['password'] != user_password:
                return "Пароль неверный! Повторите ввод"

    return "Данного пользователя не существует"


# общая сложность O(1)
def authorization_2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:
            return (f'Пользователь {user_name} допущен к ресурсу.')
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:
            return (f'Пользователь {user_name} не допущен к ресурсу. Необходимо пройти аутентификацию.')
        elif users[user_name]['password'] != user_password:
            return "Пароль неверный! Повторите ввод"
    else:
        return "Данного пользователя не существует"


users = {'Alex': {'password': 'qwerty', 'activation': True},
         'Mark': {'password': 'git223', 'activation': False},
         'Kate': {'password': 'zxc55667', 'activation': True},
         'Clark': {'password': 'cool777', 'activation': False}
         }

print(authorization_1(users, 'Mark', 'git223'))
print(authorization_2(users, 'Clark', '12345'))


"""
Второе решение эффективнее, 
так как в ней не используется цикл, 
поиск в словаре по ключу имеет сложность - O(1)
"""