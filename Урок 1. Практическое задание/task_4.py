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
    "Andrey": {"Password": "123456",
               "Activate": True},
    "Kiril": {"Password": "654321",
              "Activate": False},
    "Yuri": {"Password": "135246",
             "Activate": True},
    "Alex": {"Password": "246135",
             "Activate": False},
    "Mikhail": {"Password": "531642",
                "Activate": True}
}


def log_in_v1(users_list=users):  # O(n^2)
    username = input('Your login: ')  # O(1)
    password = input('Your password: ')  # O(1)
    if users_list.get(username):  # O(1)
        if users_list[username]['Password'] == password and users_list[username]['Activate']:  # O(n)
            return print('Вход осуществлен')  # O(1)
        elif users_list[username]['Password'] == password and not users_list[username]['Activate']:  # O(n)
            return print('У вас не активирован аккаунт!')  # O(1)
        else:
            return print('Пароль введен неверно!')  # O(1)
    else:
        return print('Такого пользователя не существует!')  # O(1)


log_in_v1()


def log_in_v2(login, password, users_list=users):                               # 0(n)
    for key, value in users_list.items():                                       # O(n)
        if key == login:                                                        # O(1)
            if value['Password'] == password and value['Activate'] is True:     # O(1)
                return print('Вход осуществлен')                                # O(1)
            elif value['Password'] == password and value['Activate'] is False:  # O(1)
                return print('У вас не активирован аккаунт!')                   # O(1)
            elif value['Password'] != password:                                 # O(1)
                return print('Пароль введен неверно!')                          # O(1)
    return print('Такого пользователя не существует!')                          # O(1)


log_in_v2('Andrey', '123456')
log_in_v2('Daniil', '123456')
log_in_v2('Andrey', '124356')
log_in_v2('Kiril', '654321')
