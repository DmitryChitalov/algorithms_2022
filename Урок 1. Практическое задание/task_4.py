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


bd_users = {'user1': {'password': '1123', 'activation': True},
            'user2': {'password': '11234', 'activation': False},
            'user3': {'password': '1123456', 'activation': True},
            'user4': {'password': '1789', 'activation': False}
           }


def authorization_1(user_name, user_password):  # O(n)
    for key, value in bd_users.items():  # O(n)
        if key == user_name:  # O(1)
            if value['password'] == user_password and value['activation']:   # O(1)
                return "Добро пожаловать! Доступ к ресурсу предоставлен"   # O(1)
            elif value['password'] == user_password \
                    and not value['activation']:    # O(1)
                return f"Учетная запись {user_name} не активна! Пройдите активацию!"  # O(1)
            elif value['password'] != user_password:
                return "Пароль не верный"   # O(1)
    return f"Пользователя {user_name} не существует"   # O(1)


def authorization_2(user_name, user_password):  # O(1)
    if bd_users.get(user_name):   # O(1)
        if bd_users[user_name]['password'] == user_password \
                and bd_users[user_name]['activation']:
            return "Добро пожаловать! Доступ к ресурсу предоставлен"   # O(1)
        elif bd_users[user_name]['password'] == user_password \
                and not bd_users[user_name]['activation']:   # O(1)
            return f"Учетная запись {user_name} не активна! Пройдите активацию!"
        elif bd_users[user_name]['password'] != user_password:
            return "Пароль не верный"   # O(1)
    else:
        return f"Пользователя {user_name} не существует"


"""
Вторая реализация быстрее, т.к. метод get имеет сложность О(1)
"""




print(authorization_1('user6', '1111'))
print(authorization_2('user6', '1111'))