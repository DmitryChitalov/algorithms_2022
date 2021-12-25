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
print('------------------------ 1-е решение ------------------------')

service_db = [{'login': 'Human3000', 'password': 'asd12dasd', 'auth': True},
              {'login': 'Guy123', 'password': 'asdad2123asd', 'auth': False},
              {'login': 'Humblealx', 'password': 'asd83fj291d', 'auth': True}]  #O(1)

'''
#O(n)
'''
def auth_in_service(login, password):
    message = f'\nДобро пожаловать! \n{login}' #O(1)

    for user in service_db: #O(n)
        if user['login'] == login and user['password'] == password: #O(1)
            auth = user['auth'] #O(1)
            break
        else:
            auth = None #O(1)

    # print(auth)

    if auth is None: #O(1)
        message = '\nНеправльны логин или пароль' #O(1)
    elif not auth: #O(1)
        message = '\nДля допуска к ресурсу, вам нужно активировать свою учётную запись!' #O(1)

    return message #O(1)


print(auth_in_service('Human3000', 'asd12dasd'))
print(auth_in_service('Guy123', 'asdad2123asd'))
print(auth_in_service('Guy123', 'asdad2123asdфыв'))


print('------------------------ 2-е решение ------------------------')

service_db = ['Human3000', 'asd12dasd', True,
              'Guy123', 'asdad2123asd', False,
              'Humblealx', 'asd83fj291d', True]

'''
#O(n)
'''
def auth_in_service_2(login, password):
    message = f'\nДобро пожаловать! \n{login}' #O(1)

    if not login in service_db or not password in service_db: #O(n)
        message = '\nНеправльны логин или пароль' #O(1)
    elif login in service_db and service_db.index(login)+1 == service_db.index(password) and service_db[service_db.index(password)+1] != True: #O(n)
        message = '\nДля допуска к ресурсу, вам нужно активировать свою учётную запись!' #O(1)

    return message


print(auth_in_service_2('Human3000', 'asd12dasd'))
print(auth_in_service_2('Guy123', 'asdad2123asd'))
print(auth_in_service_2('Guy123', 'asdad2123asdф'))
