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


def resource(login, password):
    dict_login = {'Igor': 1234,                    #O(n)
                   'Alexey': 4321,
                   'Artyr': 4444,
                   'Kate': 2252,
                   'July': 1478,
                   'Petynya': 7985}
    dict_activ = {'Igor': 'activated',             #O(n)
                  'Alexey': 'non-activated',
                  'Artyr': 'non-activated',
                  'Kate': 'activated',
                  'July': 'activated',
                  'Petynya': 'activated'}
    if password == dict_login[login]:              #O(1)
        if dict_activ[login] == 'activated':       #O(1)
            print('Вход разрешен')                 #O(1)
        else:
            print('Пройдите активацию')            #O(1)

    else:
        print('Wrong password')                    #O(1)


resource('Igor', 1234)

"""Сложность функции resourse2 O(n**2)"""


def resource2(login, password):
    dict_login = {'Igor': 1234,                    #O(n)
                   'Alexey': 4321,
                   'Artyr': 4444,
                   'Kate': 2252,
                   'July': 1478,
                   'Petynya': 7985}                                 #O(n)
    dict_activ = {'Igor': 'activated',             #O(n)
                  'Alexey': 'non-activated',
                  'Artyr': 'non-activated',
                  'Kate': 'activated',
                  'July': 'activated',
                  'Petynya': 'activated'}                                 #O(n)
    users_activated = []                               #O(1)
    if login in dict_login.keys():                         #O(n)
        if password == dict_login[login]:                         #O(1)
            for key, values in dict_activ.items():     #O(n)
                if values == 'activated':              #O(1)
                    users_activated.append(key)        #O(1)
        else:
            print('Wrong password')                    #O(1)
            exit()                                     #O(1)
        if login in users_activated:                       #O(n)
            print('activated')                         #O(1)
        else:
            print('Пройдите активацию')                #O(1)
    else:
        print('Wrong login')                           #O(1)


resource2('Alexey', 4321)
