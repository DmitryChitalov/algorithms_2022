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

Самое эффективное решение -- def check_activate_03, так как у него константная сложность
"""
users_data = {'user_1': {'password': 'pass_1', 'activation': True},
              'user_2': {'password': 'pass_2', 'activation': False},
              'user_3': {'password': 'pass_3', 'activation': False}}


def check_activate_01(login, password, data=users_data):  # O(n)
    for key, value in data.items():  # O(n)
        if key == login:  # O(1)
            if value['password'] == password and value['activation'] is True:  # O(1)
                return print('Activation complete')  # O(1)
            elif value['password'] == password and value['activation'] is False:  # O(1)
                return print('Please, activate your account')  # O(1)
            elif value['password'] != password:  # O(1)
                return print('Password is incorrect')  # O(1)
    return print('Please, register your account')  # O(1)


check_activate_01('user_1', 'pass_1')
check_activate_01('user_2', 'pass_2')
check_activate_01('user_3', 'pass_4')
check_activate_01('user_33', 'pass_4')


data_list = [['user_1', 'pass_1', True], ['user_2', 'pass_2', False], ['user_4', 'pass_3', True]]


def check_activate_02(data=data_list):  # O(n)
    login = input('Your login: ')  # O(1)
    password = input('Your password: ')  # O(1)
    if [login, password, True] in data:  # O(n)
        result = 'Activation complete'  # O(1)
    elif [login, password, False] in data:  # O(n)
        result = 'Please, activate your account'  # O(1)
    else:  # O(n)
        result = 'User not found. Please, register your account'  # O(1)
    return print(result)  # O(1)


check_activate_02()


def check_activate_03(data=users_data):  # O(1)
    user_name = input('Your login: ')  # O(1)
    user_password = input('Your password: ')  # O(1)
    if data.get(user_name):  # O(1)
        if data[user_name]['password'] == user_password and data[user_name]['activation']:  # O(1)
            return print('Activation complete')  # O(1)
        elif data[user_name]['password'] == user_password and not data[user_name]['activation']:  # O(1)
            return print('Please, activate your account')  # O(1)
        else:  # O(1)
            return print('Login or password is incorrect')  # O(1)
    else:   # O(1)
        return print('User not found. Please, register your account')  # O(1)


check_activate_03()

