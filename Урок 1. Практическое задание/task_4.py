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
    'user_1': {'password': 'qwerty', 'activity': 'yes'},
    'user_2': {'password': '344565678', 'activity': 'no'},
    'user_3': {'password': 'dsdfgderwer', 'activity': 'yes'},
    'user_4': {'password': 'dasd324dfgA', 'activity': 'yes'}
}


def user_auth_1(users, user_name, password):
    """Функция для авторизации пользователя

    Алгоритм 1:
    Авторизация пользователя происходит через ветвление

    Сложность: O(1)
    """
    if user_name in users:  # O(1)
        # O(1)
        if password == users[user_name]['password'] and users[user_name]['activity'] == 'yes':
            return f'Добрый день {user_name}, доступ разрешен'  # O(1)
        # O(1)
        elif password == users[user_name]['password'] and users[user_name]['activity'] == 'no':
            return f'{user_name} вам необходимо завершить активацию'  # O(1)
        elif password != users[user_name]['password']:  # O(1)
            return f'Неверный пароль, повторите еще раз'  # O(1)
    else:  # O(1)
        return 'Неверное имя пользователя'  # O(1)


def user_auth_2(users, user_name, password):
    """Функция для авторизации пользователя

    Алгоритм 2:
    Авторизация пользователя происходит через цикл, проходимся по всем данным, ищем нужную строку, с дальнейшим ветвлением

    Сложность: O(n)
    """
    for k, v in users.items():  # O(n)
        if k == user_name:  # O(1)
            if v['password'] == password and v['activity'] == 'yes':  # O(1)
                return f'Добрый день {user_name}, доступ разрешен'
            elif v['password'] == password and v['activity'] == 'no':  # O(1)
                return f'{user_name} вам необходимо завершить активацию'
            elif password != users[user_name]['password']:  # O(1)
                return f'Неверный пароль, повторите еще раз'
    else:  # O(1)
        return 'Неверное имя пользователя'


print((user_auth_1(users, 'user_1', 'qwerty')))
print((user_auth_1(users, 'user_2', '344565678')))
print((user_auth_1(users, 'user_4', 'dasd324d')))
print((user_auth_1(users, 'user_5', 'qwerty')))

print((user_auth_2(users, 'user_1', 'qwerty')))
print((user_auth_2(users, 'user_2', '344565678')))
print((user_auth_2(users, 'user_4', 'dasd324d')))
print((user_auth_2(users, 'user_5', 'qwerty')))

"""
Написано 2 функции, 1-й алгоритм имеет наименьшую сложность, так как поиск по ключу в словаре имеет констатный тип
"""
