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

users = {'Narin': ['1234', True], 'Mowyn': ['1234', True], 'Sarim': ['1234', False],
         'Saidi': ['1234', True], 'Donos': ['1234', False], 'Darus': ['1234', True],
         'Kazik': ['1234', True]}


def identification1(user, password, dict1):  # O(n)
    if user not in dict1:  # O(n)
        print('Unknown user')  # O(1)
    elif password != dict1[user][0]:  # O(1)
        print('Wrong password')  # O(1)
    elif not dict1[user][1]:  # O(1)
        print(user, ', activate your account, please')  # O(1)
    else:
        print("Welcome,", user)  # O(1)


identification1('Sarim', '1234', users)


def identification2(user, password, dict1):  # O(1)
    try:
        if password != dict1[user][0]:  # O(1)
            print('Wrong password')  # O(1)
        elif not dict1[user][1]:  # O(1)
            print(user, ', activate your account, please')  # O(1)
        else:
            print("Welcome,", user)  # O(1)
    except:
        print('Unknown user', user)  # O(1)


identification2('Qwerty', '1234', users)

# Второе решение эффективнее, тк у него самая низкая сложность
