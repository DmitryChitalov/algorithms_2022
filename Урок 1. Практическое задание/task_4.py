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

users = {'user1': {'pass': '1111', 'activation': True}, 'user2': {'pass': '2222', 'activation': False},
         'user3': {'pass': '3333', 'activation': True}, 'user4': {'pass': '4444', 'activation': False}}


def check_login(login):                                         #O(1)
    return login in users.keys()


def check_activation(login):                                    #O(1)
    return users[login]['activation']


def check_pass(login, passw):                                   #O(1)
    return users[login]['pass'] == passw


def main1():                  #returns True or False            # O(1)
    login = input('Введите логин: ')
    if check_login(login):                                      # O(1)
        passw = input('Введите пароль: ')
        if check_pass(login, passw):                            # O(1)
            if check_activation(login):                         # O(1)
                print('Добро пожаловать!')
                return True
            else:
                print('Учетная запись не активирована. Пожалуйста завершите активацию и попробуйте снова.')
                return False
        else:
            print('Неверный пароль.')
            return False
    else:
        print(f'Пользователь {login} не найден. Пройдите регистрацию.')


main1()


###################


def authentification2():                                # O(n) + O(1) + O(1) + O(1) = O(n)
    login = input('Введите логин: ')
    for el in users:                                    # O(n)
        if login == el:                                 # O(1)
            passw = input('Введите пароль: ')
            if passw in users[login].values():          # O(1)
                if True in users[login].values():       # O(1)
                    return 'Authentication passed'
                else:
                    return 'Please finish activation'
            else:
                return 'Incorrect password'
    return 'Incorrect login'


print(authentification2())
