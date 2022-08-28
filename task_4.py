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


users = {'John': {'password': 'Lennon', 'status': True}, 'Paul': {'password': 'McCartney', 'status': False}, 'Jim': {'password': 'Morisson', 'status': True}}

# print(users['John']['password'])
def auth1(username, password): #O(1)
    if users.get(username):
        if users[username]['password'] != password:
            return 'Access denied'
        elif users[username]['password'] == password and users[username]['status']:
            return 'Access granted'
        elif users[username]['password'] == password and not users[username]['status']:
            return 'User is not activated'
    else:
        return 'User does not exist'

def auth2(username, password): #O(n)
    for key, val in users.iterms():
        if key == username:
            if val['password'] != password:
                return 'Access denied'
            elif val['password'] == password and val['status']:
                return 'Access granted'
            elif val['password'] == password and not val['status']:
                return 'User is not activated'
        else:
            return 'User does not exist'
print('print using auth1 def')
print(auth1('Jim', 'Morisson'))
print(auth1('Paul', 'McCartney'))
print(auth1('John', 'Lenonov'))
print(auth1('Vasya', 'fyvaprodzh'))
print('/'*50)

print('print using auth2 def')
print(auth1('Jim', 'Morisson'))
print(auth1('Paul', 'McCartney'))
print(auth1('John', 'Lenonov'))
print(auth1('Vasya', 'fyvaprodzh'))
