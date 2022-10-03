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

users = {'a': {'pas': '1', 'act': 1},
         'b': {'pas': '2', 'act': 1},
         'c': {'pas': '3', 'act': 1},
         'd': {'pas': '4', 'act': 0},
         'e': {'pas': '5', 'act': 0}
         }


# Проверка 1. Сложность O(1)
def login_check1(user_log, user_pass, user_dict):
    if user_dict[user_log]['pas'] == user_pass and user_dict[user_log]['act'] == 1:
        return 'Аккаунт активирован'
    elif user_dict[user_log]['pas'] != user_pass and user_dict[user_log]['act'] == 1:
        return 'Неверный пароль'
    elif user_dict[user_log]['pas'] == user_pass and user_dict[user_log]['act'] != 1:
        return 'Аккаунт не активирован. Пройдите активацию'

# Проверка 2. Сложность O(n^2)
def login_check2(user_log, user_pass, user_dict):
    for key, val in user_dict.items():
        if key == user_log:
            flag, flag1 = False, False
            for key_m, val_m in val.items():
                if flag:
                    if val_m == 1:
                        flag1 = True
                        return 'Аккаунт активирован'
                        break
                    else:
                        return 'Аккаунт не активирован. Пройдите активацию'
                        break
                else:
                    if val_m == 1 or val_m == 0:
                        flag1 = True
                        return 'Неверный пароль'
                        break
                if val_m == user_pass:
                    flag = True


login = input('Введите логин: ')
password = input('Введите пароль: ')

print('Проверка 1: ', login_check1(login, password, users))
print('Проверка 2: ', login_check2(login, password, users))


# Проверка 1 лучше потому, что ее сложность ниже и не влечет за собой большое количество операций.
