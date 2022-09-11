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
dict_users = {'user1': {'pass': 'us123', 'auth': 1},
              'user2': {'pass': 'us223', 'auth': 0},
              'user3': {'pass': 'us323', 'auth': 0}}


# первый вариант - более эффективный, т.к. меньше операций
def auth_check(dict_us, user_log, password):  # O(1)
    if user_log in dict_us.keys():  # O(1)
        if dict_us[user_log]['pass'] == password:  # O(1)
            if dict_us[user_log]['auth'] == 0:  # O(1)
                return f'Пользователю {user_log} необходимо активировать учетную запись.'
            else:
                return f'Пользователь {user_log}, добро пожаловать!'
        else:
            return f'У пользователя {user_log} неверный пароль.'
    else:
        return f'Пользователя {user_log} не существует.'


print(auth_check(dict_users, 'user1', 'us123'))
print(auth_check(dict_users, 'user2', 'us223'))
print(auth_check(dict_users, 'user3', 'us111'))
print(auth_check(dict_users, 'user4', '00000'))


# второй вариант
def auth_check2(dict_us, user_log, password):
    for key, value in dict_us.items():  # O(n)
        if key == user_log:  # O(1)
            if value['pass'] == password:  # O(1)
                if value['auth'] == 1:  # O(1)
                    return f'Пользователь {user_log}, добро пожаловать!'
                else:
                    return f'Пользователю {user_log} необходимо активировать учетную запись.'
            else:
                return f'У пользователя {user_log} неверный пароль.'
    return f'Пользователя {user_log} не существует.'


print(auth_check2(dict_users, 'user1', 'us123'))
print(auth_check2(dict_users, 'user2', 'us223'))
print(auth_check2(dict_users, 'user3', 'us111'))
print(auth_check2(dict_users, 'user4', '00000'))




