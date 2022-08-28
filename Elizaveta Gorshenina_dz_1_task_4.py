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

USERS_INFO = {'JohnB': {'password': '2022newpass', 'status': 1},
              'Cassandra': {'password': '919358hhTTg', 'status': 0},
              'valentine': {'password': '_tt_yyy_777_', 'status': 1}}


# 1 решение. Сложность: O(N)
def authentication_proc_1(user_name, password):
    for key, value in USERS_INFO.items():                       # O(N)
        if key == user_name:                                    # O(1)
            if value['password'] == password:                   # O(1)
                if value['status']:                             # O(1)
                    return 'Welcome!'                           # O(1)
                else:
                    return 'Please authorise your account.'     # O(1)
            else:
                return 'Password is incorrect.'                 # O(1)
    return 'There is no such user.'                             # O(1)


print(authentication_proc_1('JohnB', '_tt_yyy_777_'))
print(authentication_proc_1('Cassandra', '919358hhTTg'))
print(authentication_proc_1('valentine', '_tt_yyy_777_'))


# 2 решение. Сложность: # O(1)
def authentication_proc_2(user_name, password):
    if USERS_INFO.get(user_name):                           # O(1)
        if USERS_INFO[user_name]['password'] == password:   # O(1)
            if USERS_INFO[user_name]['status']:             # O(1)
                return 'Welcome!'                           # O(1)
            else:
                return 'Please authorise your account.'     # O(1)
        else:
            return 'Password is incorrect.'                 # O(1)
    return 'There is no such user.'                         # O(1)


print(authentication_proc_2('JohnB', '_tt_yyy_777_'))
print(authentication_proc_2('Cassandra', '919358hhTTg'))
print(authentication_proc_2('valentine', '_tt_yyy_777_'))

# Решение 2 эффективнее, т.к. его сложность ниже.
