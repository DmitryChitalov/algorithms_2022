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

import random

class User:
    def __init__(self, login, password, *, is_active):
        self.login = login
        self.password = password
        self.is_active = is_active


class WebResource:
    users = {}

# identification_authentication_1 ==> O(1)
# Луший вариант, так как обработка входа пользователя 
# проходит за константое время, # так как пользователь 
# ищется в словаре по ключу
def identification_authentication_1(web_resource): # O(1)
    while True: # O(1)
        login = input("Введите логин: ") # O(1)
        password = input("Введите пароль: ") # O(1)
        try: # O(1)
            user = web_resource.users[login] # O(1)
        except KeyError: # O(1)
            print('Пользователь не найден') # O(1)
            continue # O(1)

        if user.password == password: # O(1)
            if user.is_active: # O(1)
                print('Вход разрешен') # O(1)
                return user # O(1)
            else: # O(1)
                print('Учетную запись необходимо активировать') # O(1)
                user.email = input('Для активаци введите почтовый адрес: ') # O(1)    
                activation_key = random.randint(500, 999) # O(1)
                print(f'{user.email}: Ваш ключ активации: {activation_key}') # O(1)
                while True: # O(1)
                    user_key = int(input('Введите ключ активации, который пришел вам на почту: ')) # O(1)
                    if user_key == activation_key: # O(1)
                        print('Вход разрешен') # O(1)
                        return user # O(1)
                    else: # O(1)
                        print('Ключ не верный!') # O(1)
        else: # O(1)
            print('Пароль не верен, повторите еще раз!') # O(1)


# identification_authentication_2 ==> O(n)
# Обработка входа пользователя проходит время зависящая 
# от количества пользователей, 
# так как пользователь ищется списке
def identification_authentication_2(web_resource):
    authentication_passed = False # O(1)
    while not authentication_passed: # O(1)
        login = input("Введите логин: ") # O(1)
        password = input("Введите пароль: ") # O(1)
        for user in web_resource.users: # O(n)
            if user.login == login: # O(1)
                if user.password != password: # O(1)
                    print('Пароль не верен, повторите еще раз!') # O(1)
                    break # O(1)
                else: # O(1)
                    authentication_passed = True # O(1)
                    break # O(1)
        else: # O(1)
            print('Пользователь не найден!') # O(1)
    if user.is_active: # O(1)
        print('Вход разрешен') # O(1)
        return user # O(1)
    else: # O(1)
        print('Учетную запись необходимо активировать') # O(1)
        user.email = input('Для активаци введите почтовый адрес: ') # O(1)    
        activation_key = random.randint(500, 999) # O(1)
        print(f'{user.email}: Ваш ключ активации: {activation_key}') # O(1)
        while True: # O(1)
            user_key = int(input('Введите ключ активации, который пришел вам на почту: ')) # O(1)
            if user_key == activation_key: # O(1)
                print('Вход разрешен') # O(1)
                return user # O(1)
            else: # O(1)
                print('Ключ не верный!') # O(1)



ivanov = User('Ivanov', 'i123', is_active=True)
petrov = User('Petrov', 'p123', is_active=False)
sidorov = User('Sidorov', 's123', is_active=True)
demidov = User('Demidov', 'd123', is_active=False)

web_resource = WebResource()
for u in [ivanov, petrov, sidorov, demidov]:
    web_resource.users[u.login] = u
# identification_authentication_1(web_resource)

web_resource.users = []
for u in [ivanov, petrov, sidorov, demidov]:
    web_resource.users.append(u)
identification_authentication_2(web_resource)

