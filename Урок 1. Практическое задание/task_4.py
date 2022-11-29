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
    "Все операции имеют константную сложность => алгоритм имеет консонантную сложность"
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
        elif pswd != usrs[usr][0]:
            print('wrong password')
        elif usrs[usr][1] == 1:
            print('everything is ok')
            return
        else:
            print('You have to activate your account')


def auth_2(usrs):
    "Сложность O(n)"
    usr = input('enter your login: ')  # O(1)
    pswd = input('enter your passwd: ')  # O(1)
    for key, value in usrs.items():  # O(n)
        if usr == key:
            if pswd == value[0] and value[1] == 1:
                print('everything is ok')  # O(1)
            elif pswd == value[0] and value[1] == 0:
                print('You have to activate your account')  # O(1)
            else:
                print('wrong password')  # O(1)
    print('wrong login')  # O(1)
