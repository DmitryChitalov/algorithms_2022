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

users = {'ivan': (123, True),
         'igor': (456, False),
         'vlad': (789, True)}


def user_checker_1():                                       # O(N)
    name = input('Insert your account: ')

    if name in users.keys():                                # O(N)
        password = int(input('Insert your password: '))

        if users[name][0] == password and users[name][1]:   # O(1)
            print(f'Welcome, {name}')
        else:
            print('This account is not activate. '
                  'Please check your email for activation')

    else:
        print('This account is not exists. '
              'Please register it')


def user_checker_2():                                       # O(1)
    name = input('Insert your account: ')

    if users.get(name) is not None:                         # O(1)
        password = int(input('Insert your password: '))

        if not users[name][1]:                              # O(1)
            print('This account is not activate. '
                  'Please check your email for activation')
        elif users[name][0] == password:                    # O(1)
            print(f'Welcome, {name}')
        else:
            print('Wrong password!')

    else:
        print('This account is not exists. '
              'Please register it')


def user_checker_3():
    name = input('Insert your account: ')

    for account, data in users.items():                     # O(N)
        password = int(input('Insert your password: '))
        if account == name and data[1]:                     # O(1)
            if data[0] == password:                         # O(1)
                print(f'Welcome, {name}')
            else:
                print('Wrong password!')
        elif not data[1]:                                   # O(1)
            print('This account is not activate. '
                  'Please check your email for activation')
        else:
            print('This account is not exists. '
                  'Please register it')


user_checker_1()
user_checker_2()
user_checker_3()

"""Из представленных решений оптимальное второе, так как
не используются функции перебора элементов словаря"""
