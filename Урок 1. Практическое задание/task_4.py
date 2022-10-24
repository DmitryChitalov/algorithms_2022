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
    'user1': {'password': '12345', 'activation': True},
    'user2': {'password': '12345', 'activation': False},
    'user3': {'password': '12345', 'activation': True},
    'user4': {'password': '12345', 'activation': False},
    'user5': {'password': '12345', 'activation': True}
}


# O(n)
def user_check(users, user_name, user_password):
    for k, v in users.items():  # O(n)
        if k is user_name:  # O(1)
            if v['password'] is user_password and v['activation']:  # O(1)
                return 'Вход разрешен'  # O(1)
            elif v['password'] is user_password and not v['activation']:  # O(1)
                return 'Ваш профиль не активирован'  # O(1)
            elif v['password'] is not user_password:  # O(1)
                return 'Неверный пароль'  # O(1)
    return 'Неверное имя пользователя'  # O(1)


# O(1)
def user_check2(users, user_name, user_password):
    if users.get(user_name):  # O(1)
        if users[user_name]['password'] is user_password and users[user_name]['activation']:  # O(1)
            return 'Вход разрешен'  # O(1)
        elif users[user_name]['password'] is user_password and not users[user_name]['activation']:  # O(1)
            return 'Ваш профиль не активирован'  # O(1)
        elif users[user_name]['password'] is not user_password:  # O(1)
            return 'Неверный пароль'  # O(1)
    else:  # O(1)
        return 'Неверное имя пользователя'  # O(1)


# второй вариант будет лучше так как при выполнении затрачивает меньше ресурсов

print(user_check(users, 'user1', '12345'))
print(user_check(users, 'user2', '12345'))
print(user_check(users, 'user3', '10000'))
print(user_check(users, 'user6', '12345'))

print(user_check2(users, 'user1', '12345'))
print(user_check2(users, 'user2', '12345'))
print(user_check2(users, 'user3', '10000'))
print(user_check2(users, 'user6', '12345'))
