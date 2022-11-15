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
    'Rbhnelsd': ['fn2f47e64@', True],
    'Champion88': ['1234', False],
    'Ivan_CH_25': ['IvanChernysh', False],
    'User21187': ['21927dwhs76z!354', True],
    'Kubi1979': ['nu23ed76$$2J', False],
    'Julia_Mesh': ['zx,La[qq];Z9865', False]
        }


def authentication_1(users_dict, login):                                                              # O(n)
    activation_check = None                                                                           # O(1)
    for k in users_dict.keys():                                                                       # O(n)
        if k == login:                                                                                # O(1)
            activation_check = users_dict[k][1]                                                       # O(1)
    if activation_check is False:                                                                     # O(1)
        answer = ''                                                                                   # O(1)
        while answer not in {'Y', 'N'}:                                                               # O(1)
            answer = input('Учётная запись не активирована. Активировать учётную запись (Y/N)?\n')    # O(1)
            if answer == 'Y':                                                                         # O(1)
                users_dict[login][1] = True                                                           # O(1)
                print('Учётная запись активирована.')                                                 # O(1)
            elif answer == 'N':                                                                       # O(1)
                print('Учётная запись не активирована.')                                              # O(1)
    elif activation_check is True:                                                                    # O(1)
        print('Учётная запись активирована.')                                                         # O(1)
    else:
        print('Такой учётной записи не существует.')                                                  # O(1)


def authentication_2(users_dict, login):                                                              # O(1)
    activation_check = None                                                                           # O(1)
    if login in users_dict:                                                                           # O(1)
        activation_check = users_dict[login][1]                                                       # O(1)
    if activation_check is False:                                                                     # O(1)
        answer = ''                                                                                   # O(1)
        while answer not in {'Y', 'N'}:                                                               # O(1)
            answer = input('Учётная запись не активирована. Активировать учётную запись (Y/N)?\n')    # O(1)
            if answer == 'Y':                                                                         # O(1)
                users_dict[login][1] = True                                                           # O(1)
                print('Учётная запись активирована.')                                                 # O(1)
            elif answer == 'N':                                                                       # O(1)
                print('Учётная запись не активирована.')                                              # O(1)
    elif activation_check is True:                                                                    # O(1)
        print('Учётная запись активирована.')                                                         # O(1)
    else:
        print('Такой учётной записи не существует.')                                                  # O(1)


authentication_1(users, 'Champion88')
authentication_2(users, 'Kubi1979')
print(users['Champion88'][1], users['Kubi1979'][1])

# Эффективнее решение 2 (функция authentication_2),
# т.к. оно выполняется за константное время (1),
# в отличие от решения 1, которое выполняется за линейное время (n).
