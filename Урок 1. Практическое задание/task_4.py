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

# Сложность - O(n)
def authentication(users, login, password):
    for k, v in users.items():      # O(n)
        if k == login:         # O(n)
            if v['password'] == password and v['activation']:   # O(n)
                return "Доступ разрешен"        # O(n)
            elif v['password'] == password and not v['activation']:     # O(n)
                return "Пожалуйста, активируйте учетную запись"     # O(n)
            elif v['password'] != password:     # O((len(s))
                return "Неверный пароль"        # O(n)
    return "Не удалось найти пользователя"      # O(n)


# Cложность - O(1)
def authentication_о(users, login, password):
    if users.get(login):    # O(1)
        if users[login]['password'] == password and users[login]['activation']:     # O(1)
            return "Доступ разрешен"        # O(n)
        elif users[login]['password'] == password and not users[login]['activation']:       # O(1)
            return "Пожалуйста, активируйте учетную запись"     # O(n)
        elif users[login]['password'] != password:      # O(1)
            return "Неверный пароль"        # O(n)
    else:
        return "Не удалось найти пользователя"      # O(n)


users_d = {'user_1': {'password': '1234', 'activation': False},
           'user_2': {'password': '2345', 'activation': False},
           'user_3': {'password': '3456', 'activation': True},
           'user_4': {'password': '4567', 'activation': True},
           'user_5': {'password': '5678', 'activation': True},
           'user_6': {'password': '6789', 'activation': False},
           'user_7': {'password': '7890', 'activation': False}}

print(authentication(users_d, 'user_1', '3456'))
print(authentication(users_d, 'user_4', '4567'))
print(authentication_о(users_d, 'user_8', '0000'))
print(authentication_о(users_d, 'user_2', '2345'))

# Лучший вариант - 2-й, так как функция константная и обладает наименьшей сложностью.