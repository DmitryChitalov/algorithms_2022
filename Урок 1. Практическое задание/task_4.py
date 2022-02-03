"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

users = {
        "salmon91": {"Password": '132455', "activated": True},
        "volanderbrod": {"Password": 'zver', "activated": False},
        "anna1993": {"Password": 'crew', "activated": True},
        "godfather": {"Password": 'zxcvb', "activated": False},
        "turboboy": {"Password": 'qwerty', "activated": False},
        "grizly": {"Password": '24194', "activated": True},
        }


def check_authorization1(users_lst, user_name, user_password):  # Общая сложность O(1)
    if users_lst.get(user_name):  # O(1)
        if users_lst[user_name]['Password'] == user_password and users_lst[user_name]['activated']:  # O(1)
            return "Учетная запись активирована!"  # O(1)
        elif users_lst[user_name]['Password'] == user_password and not users_lst[user_name]['activated']:  # O(1)
            return "Учетная запись не активирована. Необходимо пройти активацию!"  # O(1)
        elif users_lst[user_name]['Password'] != user_password:  # O(1)
            return "Неправельный пароль. Повторите попытку!"  # O(1)


def check_authentication2(user_lst, user_name, user_password):  # O(n)
    for key, value in user_lst.items():  # O(n)
        if key == user_name:  # O(1)
            if value['Password'] == user_password and value['activated']:  # O(1)
                return "Учетная запись активирована!"  # O(1)
            elif value['Password'] == user_password and not value['activated']:  # O(1)
                return "Учетная запись не активирована. Необходимо пройти активацию!"  # O(1)
            elif value['Password'] != user_password:  # O(1)
                return "Неправельный пароль. Повторите попытку!"  # O(1)
    return "Пользователь не найден!"  # O(1)


print(check_authorization1(users, "salmon91", "132455"))
print(check_authorization1(users, "volanderbrod", "zver"))
print(check_authorization1(users, "anna1993", "crew"))
print(check_authentication2(users, "godfather", "zxcvb"))
print(check_authentication2(users, "turboboy", "qwerty"))
print(check_authentication2(users, "grizly", "24194"))

# Превый алгоритм имеет константную сложность и будет иметь одинаковое время выполнения не зависимо от размера данных.
