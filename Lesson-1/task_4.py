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
    'alpha': {'psw': 'a111', 'activation': True},
    'beta': {'psw': 'b123', 'activation': True},
    'gamma': {'psw': 'g000', 'activation': False}
    }


# Простое решение с хорошей константной сложностью O(1), хотя тоже с ветвлением:


def authorization_check(users, login, psw):
    if users.get(login):                                                     # O(1)
        if users[login]['psw'] == psw and users[login]['activation']:        # O(1)
            return 'Доступ разрешен'                                         # O(1)
        elif users[login]['psw'] == psw and not users[login]['activation']:  # O(1)
            return 'Учётная запись не активирована, подтвердите учетную запись для входа'  # O(1)
        elif users[login]['psw'] != psw:                                     # O(1)
            return 'Пароль неверный'                                         # O(1)
    else:                                                                    # O(1)
        return 'Пользователь не найден'                                      # O(1)


# Решение с ветвлением, сложность  O(n)


def authorization_check1(users, login, psw):
    for key, value in users.items():                                         # O(n)
        if key == login:                                                     # O(1)
            if value['psw'] == psw and value['activation']:                  # O(1)
                return 'Доступ разрешен'                                     # O(1)
            elif value['psw'] == psw and not value['activation']:            # O(1)
                return 'Учётная запись не активирована, подтвердите учетную запись для входа'  # O(1)
            elif value['psw'] != psw:                                        # O(1)
                return 'Пароль неверный'                                     # O(1)
    else:                                                                    # O(1)
        return 'Пользователь не найден'                                      # O(1)


print(authorization_check(users, 'alpha', 'a111'))
print(authorization_check(users, 'alpha', 'a123'))
print(authorization_check(users, 'gamma', 'g000'))
print(authorization_check1(users, 'beta', 'b123'))
print(authorization_check1(users, 'betha', 'b123'))
print(authorization_check1(users, 'gamma', 'g000'))

# Вывод: решение с константной сложностью O(1) лучше второго с O(n)
