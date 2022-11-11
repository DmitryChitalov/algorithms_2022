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


def users_check_1(users, login):   # O(n)
    if login not in users.keys():    # O(n)
        msg = f'User {login} is not added. Please register to access the resource.'     # O(1)
    elif not users.get(login).get('activation'):    # O(1)
        msg = f'User {login} is not activated. Please activate account to access the resource.'     # O(1)
    else:   # O(1)
        msg = f'Dear {login}, welcome to the resourse.' # O(1)
    return msg      # O(1)


def users_check_2(users, login):   # O(n)
    msg = f'User {login} is not added. Please register to access the resource.'     # O(1)
    for user in users:                                          # O(n)
         if user == login:                                      # O(1)
             if users.get(user).get('activation'):              # O(1)
                 msg = f'Dear {user}, welcome to the resourse.' # O(1)
             else:                                              # O(1)
                 msg = f'User {user} is not activated. Please activate account to access the resource.'     # O(1)
    return msg      # O(1)

if __name__ == '__main__':
    users_dict = {
        'user_1': {'password': 'pass1', 'activation': True},
        'user_2': {'password': 'pass2', 'activation': False},
        'user_3': {'password': 'pass3', 'activation': True}
    }

    print(users_check_1(users_dict, 'user_1'))
    print(users_check_1(users_dict, 'user_2'))
    print(users_check_1(users_dict, 'user_3'))
    print(users_check_1(users_dict, 'user_4'))
    print('*'*50)
    print(users_check_2(users_dict, 'user_1'))
    print(users_check_2(users_dict, 'user_2'))
    print(users_check_2(users_dict, 'user_3'))
    print(users_check_2(users_dict, 'user_4'))