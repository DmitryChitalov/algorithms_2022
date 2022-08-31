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

all_users = {'user1': {'password': '11111', 'activation': True},
             'user2': {'password': '22222', 'activation': False},
             'user3': {'password': '33333', 'activation': True},
             'user4': {'password': '44444', 'activation': False}
             }


# O(1) - константная
def authorization_1(users, user_name, user_pass):
    if users.get(user_name):                                                                    # O(1)
        if users[user_name]['password'] == user_pass and users[user_name]['activation']:        # O(1)
            return "Добро пожаловать!"                                                          # O(1)
        elif users[user_name]['password'] == user_pass and not users[user_name]['activation']:  # O(1)
            return "Доступ запрещен, пройдите активацию!"                                       # O(1)
        elif users[user_name]['password'] != user_pass:                                         # O(1)
            return "Не верный пароль!"                                                          # O(1)
    else:                                                                                       # O(1)
        return "Не верный логин!"                                                               # O(1)


print(authorization_1(all_users, 'user1', '11111'))


# O(n) - линейная
def authorization_2(users, user_name, user_pass):
    for k, val in users.items():                                            # O(n)
        if k == user_name:                                                  # O(1)
            if val['password'] == user_pass and val['activation']:          # O(1)
                return "Добро пожаловать!"                                  # O(1)
            elif val['password'] == user_pass and not val['activation']:    # O(1)
                return "Доступ запрещен, пройдите активацию!"               # O(1)
            elif val['password'] != user_pass:                              # O(1)
                return "Не верный пароль!"                                  # O(1)
    else:                                                                   # O(1)
        return "Не верный логин!"                                           # O(1)


print(authorization_2(all_users, 'user2', '22222'))


"""
Первый вариант лучше, так как не используется цикл
"""