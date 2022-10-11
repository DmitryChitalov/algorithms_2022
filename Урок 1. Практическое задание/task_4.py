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


def auth(usrs):
    """
    тут всё #O(1)
    """
    while True:
        usr = input('enter your login (or 0 to exit): ')
        if usr == '0':
            return
        elif usr not in usrs:
            print('No such user')
        else:
            break

    while True:
        pswd = input('enter your password (or "x" to exit): ')
        if pswd == 'x':
            return
        elif pswd != users[usr][0]:
            print('wrong password')
        elif users[usr][1] == 1:
            print('You are a good boy')
            return
        else:
            print('You have to activate your account')
        return


def auth_2(usrs):
    """
    один цикл дает итоговое O(n), остальное O(1).
    """
    usr = input('enter your login: ')
    pswd = input('enter your passwd: ')
    for key, value in usrs.items():                     # O(N)
        if usr == key:
            if pswd == value[0] and value[1] == 1:
                print('ok')
            elif pswd == value[0] and value[1] == 0:
                print('activate your account please')
            else:
                print('wrong password')
            return
    print('wrong login')
    return

# Вывод: во втором решении я специально усложнял алгоритм,
# он должен был быть хуже


if __name__ == '__main__':
    users = {
        'user_1': ['password_1', 1],
        'user_2': ['password_2', 0],
        'user_3': ['password_3', 1],
    }
    auth(users)
    auth_2(users)
