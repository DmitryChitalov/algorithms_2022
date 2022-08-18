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
    'Sam': {'password': 'qwe', 'active': True},
    'Bob': {'password': 'asd', 'active': False},
    'Billy': {'password': 'zxc', 'active': True}
}


def authorization_1(users, user_name, user_pwd):                # Сложность O(1)
    if users.get(user_name):                                    # O(1)
        if users[user_name]['password'] == user_pwd and\
                users[user_name]['active']:                     # O(1)
            return f'Вход выполнен! {user_name}'                # O(1)
        elif users[user_name]['password'] == user_pwd and\
                not users[user_name]['active']:                 # O(1)
            return f'Учетная запись {user_name} не активна!'    # O(1)
        elif users[user_name]['password'] != user_pwd:          # O(1)
            return f'Пароль пользователя {user_name} не верный'
    else:
        return f'Пользователь {user_name} не найден'            # O(1)


def authorization_2(users, user_name, user_pwd):                                  # Сложность O(n)
    for k, v in users.items():                                                    # O(N)
        if k == user_name:  # O(1)
            if v['password'] == user_pwd and v['active']:                         # O(1)
                return f'Вход выполнен! {user_name}'                              # O(1)
            elif v['password'] == user_pwd and not v['active']:
                return f'Учетная запись {user_name} не активна!'                  # O(1)
            elif v['password'] != user_pwd:                                       # O(1)
                return f'Пароль пользователя {user_name} не верный'
        else:
            return f'Пользователя {user_name} не найден'                          # O(1)


print(authorization_1(users, 'Sam', 'qwe'))
print(authorization_2(users, 'Bob', 'asd'))

"""
Вывод: алгоритм с константной сложностью более эффективен
"""
