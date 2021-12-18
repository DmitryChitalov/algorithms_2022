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

users = {'login_1': {'password': 467513, 'activated': 'yes'},
         'login_2': {'password': 745847, 'activated': 'no'},
         'login_3': {'password': 964237, 'activated': 'yes'},
         'login_4': {'password': 745896, 'activated': 'no'},
         'login_5': {'password': 314567, 'activated': 'yes'},
         }

# 1 вариант. Сложность O(1)

def verification_1(login, password):
    if users[login]['password'] == password:  # O(1)
        if users[login]['activated'] == 'yes':  # O(1)
            print('Access is allowed')  # O(1)
        else:
            print('Сomplete the activation')  # O(1)
    else:
        print('Invalid login or password')  # O(1)


verification_1('login_5', 314567)
verification_1('login_4', 745896)

# 2 вариант. Сложность O(n)

def verification_2(login, password):
    if login in users and users[login]['password'] == password:  # O(n)
        if users[login]['activated'] == 'yes':  # O(1)
            print('Access is allowed')  # O(1)
        else:
            print('Сomplete the activation')  # O(1)
    else:
        print('Invalid login or password')  # O(1)


verification_2('login_5', 314567)
verification_2('login_4', 745896)




#  Первое решение эффективнее, т.к. O(1) выполняеется быстрее, чем O(n).