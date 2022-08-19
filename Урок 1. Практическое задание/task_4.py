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

users = [
    {
        'login': 'user1',
        'pass': 'qwerty',
        'activated': False
    },
    {
        'login': 'Mark',
        'pass': '123',
        'activated': True
    },
    {
        'login': 'username',
        'pass': 'password',
        'activated': True
    }
]


##########################################################################################

def check_lin(user_list, username, password):
    """Линейная сложность"""
    for user in user_list:                                          # O(n) - линейная
        if user['login'] == username and user['pass'] == password:  # O(1) - константная
            if user['activated'] is True:                           # O(1) - константная
                return True                                         # O(1) - константная
            else:
                return False                                        # O(1) - константная
    return 'Error'                                                  # O(1) - константная


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


def bin_search(lst, user):
    """Логарифмическая сложность"""
    found = False                             # O(1) - константная
    start = 0                                 # O(1) - константная
    end = len(lst) - 1                        # O(1) - константная
    mid_index = 0                             # O(1) - константная
    while start <= end:                       # O(1) - константная
        mid_index = int((start + end) / 2)    # O(log n) - логарифмическая
        if lst[mid_index]['login'] == user:   # O(1) - константная
            found = True                      # O(1) - константная
            break                             # O(1) - константная
        elif lst[mid_index]['login'] < user:  # O(1) - константная
            start = mid_index + 1             # O(1) - константная
        else:
            end = mid_index - 1               # O(1) - константная
    if found:                                 # O(1) - константная
        return mid_index                      # O(1) - константная
    return False                              # O(1) - константная


def check_bin(lst, user, passwd):
    """Логарифмическая сложность"""
    index = bin_search(lst, user)                # O(log n) - логарифмическая
    if index:                                    # O(1) - константная
        if lst[index]['pass'] == passwd:         # O(1) - константная
            if lst[index]['activated'] is True:  # O(1) - константная
                return True                      # O(1) - константная
            else:
                return False                     # O(1) - константная
    return 'Error'                               # O(1) - константная


def auth_nlog(user_list, user, passwd):
    """Линейно-логарифмическая сложность"""
    user_list.sort(key=lambda x: x['login'])     # O(n * log n) - линейно-логарифмическая

    status = check_bin(user_list, user, passwd)  # O(log n) - логарифмическая
    if status == 'Error':                        # O(1) - константная
        return 'Wrong credentials'               # O(1) - константная
    elif status is False:                        # O(1) - константная
        return 'Please activate your account'    # O(1) - константная
    else:
        return 'User is logged in'               # O(1) - константная


##########################################################################################

print(auth_lin(users, 'username', 'password'))
print(auth_nlog(users, 'username', 'password'))

"""Вывод: алгоритм auth_lin() более оптимальный, 
т.к. имеет меньшую алгоритмическую сложность"""