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

database = {
               'users':
                   [
                   {'id': 1, 'login': 'masyanya', 'password': 'qwerty', 'status': 'activate'},
                   {'id': 2, 'login': 'erebuka', 'password': 'qweqw435y', 'status': 'activate'},
                   {'id': 3, 'login': 'teqos', 'password': 'qwefgdsrty', 'status': 'nonactivate'},
                   {'id': 4, 'login': 'metrusha', 'password': 'qwedfgerty', 'status': 'activate'},
                   {'id': 5, 'login': 'letucka', 'password': 'qweqcvzty', 'status': 'nonactivate'},
                   {'id': 6, 'login': 'neo', 'password': 'qweqzvczrty', 'status': 'nonactivate'},
                   {'id': 7, 'login': 'musya', 'password': 'qwezvcerty', 'status': 'activate'},
                   ]
}


def check_auth(dict_obj):
    '''dict_obj - входящие данные со стороны пользователя {"login": "..." , "password": "..."}'''
    for user, item_list in database.items():
        for users in item_list:
            if dict_obj['password'] != users['password']:
                return f'{dict_obj["login"]} - такого пользователя нет в системе, можете зарегестрироваться'
            elif dict_obj['login'] == users['login']:
                if dict_obj['password'] == users['password'] and users['status'] == 'activate':
                    res = f'{dict_obj["login"]} - вы допущены к ресурсу '
                    res = f'Пароль неверный'
            else:
                res = f'Пользователь не авторизован'
    return res



user = {'login': 'neo', 'password': 'qweqzvczrty'}

print(check_auth(user))

for i, j in database.items():
    for k in j:
        print(user['login'] == k['login'])

