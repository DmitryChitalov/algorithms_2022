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


def authentication_1(users, user_name, user_password):                                  # Сложность: O(1)
    if users.get(user_name):                                                            # O(1)
        if users[user_name][0] == user_password and users[user_name][1] == 'Yes':       # O(1)
            return 'Вход выполнен'                                                      # O(1)
        elif users[user_name][0] == user_password and users[user_name][1] == 'No':      # O(1)
            return 'Пройдите активацию'                                                 # O(1)
    return 'Не верное имя пользователя или пароль'                                      # O(1)


def authentication_2(users, user_name, user_password):                      # Сложность: O(n)
    for key, value in users.items():                                        # O(n)
        if key == user_name:                                                # O(1)
            if value[0] == user_password and value[1] == 'Yes':             # O(1)
                return 'Вход выполнен'                                      # O(1)
            elif value[0] == user_password and value[1] == 'No':            # O(1)
                return 'Пройдите активацию'                                 # O(1)
    return 'Не верное имя пользователя или пароль'                          # O(1)


# users = {'Max': ['password1', 'Yes'], 'Mike': ['password2', 'No'], 'Den': ['password3', 'Yes'],
#          'Alice': ['password4', 'No'], 'Sam': ['password5', 'No']}

# print(authentication_1(users, 'Max', 'password1'))
# print(authentication_1(users, 'Mike', 'password2'))
# print(authentication_1(users, 'Mike', '123213'))
# print(authentication_1(users, 'sdaads', 'password1'))
#
# print(authentication_2(users, 'Max', 'password1'))
# print(authentication_2(users, 'Mike', 'password2'))
# print(authentication_2(users, 'Mike', '123213'))
# print(authentication_2(users, 'sdaads', 'password1'))
