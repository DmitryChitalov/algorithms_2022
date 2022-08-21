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
    'user1': {
        'pass': 'qwerty',
        'activated': False
    },
    'Mark': {
        'pass': '123',
        'activated': True
    },
    'username': {
        'pass': 'password',
        'activated': True
    }
}


##########################################################################################

def check_lin(user_dict, username, password):
    """Линейная сложность"""
    for user, attribute in user_dict.items():                   # O(n) - линейная
        if user == username and attribute['pass'] == password:  # O(1) - константная
            if attribute['activated'] is True:                  # O(1) - константная
                return True                                     # O(1) - константная
            else:
                return False                                    # O(1) - константная
    return 'Error'                                              # O(1) - константная


def auth_lin(user_list, user, passwd):
    """Линейная сложность"""
    status = check_lin(user_list, user, passwd)  # O(n) - линейная
    if status == 'Error':                        # O(1) - константная
        return 'Wrong credentials'               # O(1) - константная
    elif status is False:                        # O(1) - константная
        return 'Please activate your account'    # O(1) - константная
    else:
        return 'User is logged in'               # O(1) - константная


##########################################################################################


def check_const(user_dict, user, passwd):
    """Константная сложность"""
    if user_dict.get(user) and user_dict[user]['pass'] == passwd:    # O(1) - константная
        if user_dict[user]['activated'] is True:                     # O(1) - константная
            return True                                              # O(1) - константная
        else:
            return False                                             # O(1) - константная
    return 'Error'                                                   # O(1) - константная


def auth_nlog(user_list, user, passwd):
    """Константная сложность"""
    status = check_const(user_list, user, passwd)  # O(1) - константная
    if status == 'Error':                          # O(1) - константная
        return 'Wrong credentials'                 # O(1) - константная
    elif status is False:                          # O(1) - константная
        return 'Please activate your account'      # O(1) - константная
    else:
        return 'User is logged in'                 # O(1) - константная


##########################################################################################

print(auth_lin(users, 'username', 'password'))
print(auth_nlog(users, 'username', 'password'))

"""Вывод: алгоритм auth_const() более оптимальный, 
т.к. имеет меньшую алгоритмическую сложность"""
