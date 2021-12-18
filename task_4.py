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

users = [
    {"Login": "Smith105", "Password": "smt501", "is_active": True},
    {"Login": "Alex1995", "Password": "cool500", "is_active": False},
    {"Login": "Simpson", "Password": "simpson", "is_active": False},
    {"Login": "zxcvb", "Password": "123456", "is_active": True},
    {"Login": "sweetheart", "Password": "qwerty1", "is_active": True},
    {"Login": "Lexy5", "Password": "123456789", "is_active": False},
    {"Login": "zokuli333", "Password": "ytrewq789", "is_active": True},
    {"Login": "CareyBerry", "Password": "berries", "is_active": True},
    {"Login": "Genius", "Password": "Jnshyadb903", "is_active": True}
]


# 1: O(n)
def admission(login, password):
    for i in users:                                                  # O(n)
        if i.get("Login") == login:                                  # O(n)
            if i.get("Password") == password:                        # O(n)
                if i.get("is_active"):                               # O(n)
                    return f'Access allowed'                         # O(1)
                else:
                    return f'You need to activate your account'      # O(1)
            else:
                return f'Access denied. Enter the correct password'  # O(1)


###
login_list = []
password_list = []
is_active_list = []
for i in users:
    login_list.append(i["Login"])
    password_list.append(i["Password"])
    is_active_list.append(i["is_active"])
###


# 2: O(n^2)
def admission(login, password):
    for k in login_list:                                                                        # O(n)
        for j in password_list:                                                                 # O(n^2)
            if k == login and j == password and login_list.index(k) == password_list.index(j):  # O(n)
                if is_active_list[login_list.index(k)]:                                         # O(n)
                    return f'Access allowed'                                                    # O(1)
                else:
                    return f'You need to activate your account'                                 # O(1)
            else:
                return f'Enter the correct login/password or create an account'                 # O(1)


"""
Вывод: предпочтительнее первый вариант, так как он характеризуется линейной сложностью, в отличие от
второго - у него квадратичная сложность. Следовательно, время выполнения первого алгоритма будет меньше.
"""