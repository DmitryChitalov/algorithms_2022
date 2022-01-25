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

users_data = {'Sergey':['123', True], 'Nikolay': ['321', True],'Anna': ['567', False],'Ignat':['765', False], 'Aristarkh': ['pass', False]}


# O(n)
def check_activation (data):
    [print("User " + k + " activted") if v[1] else print("User " + k + " is not activted. Access denied") for  k, v in data.items()]

check_activation(users_data)

# O(1)
def check_activation_2 (data):
    log = input ('Please enter your login: ')
    passw = input ('Please enter your password: ')
    if log not in data:
        print('There is no such user')
    elif data[log][0] == passw and data[log][1]:
        print (f'User {log} activated')
    elif data[log][0] == passw and not data[log][1]:
         print(f'User {log} is not activated. Access denied')
    elif passw != data[log][0]:
         print('Wrong password')

check_activation_2(users_data)

# check_activation_2 предпочтительнее, но в этом случае наперед известен логин и пароль,
# в отличие от первой функции, работающей перебором всех значений