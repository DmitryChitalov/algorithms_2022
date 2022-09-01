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


# Первое решение. Сложность O(1)
def authentication_1(users, user_name, user_password):
    if users.get(user_name):  # O(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']:  # O(1)
            return "Вы успешно вошли в аккаунт!"  # O(1)
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:  # O(1)
            return "Ваша учетная запись не активирована! Пожалуйста, пройдите активацию и попробуйте снова!"  # O(1)
        elif users[user_name]['password'] != user_password:  # O(1)
            return "Пароль неверный!"  # O(1)
    else:
        return "Логин неверный!"  # O(1)


# Первое решение. Сложность O(n)
def authentication_2(users, user_name, user_password):
    for key, value in users.items():  # O(n)
        if key == user_name:  # O(1)
            if value['password'] == user_password and value['activation']:  # O(1)
                return "Вы успешно вошли в аккаунт!"  # O(1)
            elif value['password'] == user_password and not value['activation']:  # O(1)
                return "Ваша учетная запись не активирована! Пожалуйста, пройдите активацию и попробуйте снова!"  # O(1)
            elif value['password'] == user_password:  # O(1)
                return "Пароль неверный!"  # O(1)
    else:
        return "Логин неверный!"  # O(1)


users_task_4 = {'Nikita': {'password': '11111', 'activation': False},
                'Roman': {'password': '22222', 'activation': True},
                'Elene': {'password': '33333', 'activation': True},
                'Ksenia': {'password': '44444', 'activation': False},
                'Victor': {'password': '55555', 'activation': True}
                }

print(authentication_1(users_task_4, 'Nikita', '11111'))
print(authentication_2(users_task_4, 'Roman', '11111'))

# Чем меньше сложность, тем эффективнее решение. В данном случае первый вариант эффективнее.
