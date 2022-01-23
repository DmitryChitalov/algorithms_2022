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


def check_login(users_list, user, password): # O(1)
    if users_list.setdefault(user, None) == None: # O(1)
        print('Нет такого пользователя')
    elif users_list[user]['password'] == password and users_list[user]['activation']: # O(1)
        print(f'Добро пожаловать, {user}')
    elif users_list[user]['password'] != password: # O(1)
         print(f'Неверный пароль!')
    else: # O(1)
         print(f'Учетная запись {user} не активирована')
    

def check_login2(users_list, user, password): # O(n)
    for key, value in users_list.items(): # O(n)
        if key == user:
            if value['password'] == password and value['activation']: # O(1)
                print(f'Добро пожаловать, {user}')
                break
            elif value['password'] != password: # O(1)
                print(f'Неверный пароль!')
                break
            else: # O(1)
                print(f'Учетная запись {user} не активирована')
                break
    print('Нет такого пользователя')
    

my_users = {'user1': {'password': '11111', 'activation': True},
            'user2': {'password': '11111', 'activation': False},
            'user3': {'password': '11111', 'activation': True},
            'user4': {'password': '11111', 'activation': False}
            }

check_login(my_users, 'user1', '11111')
check_login2(my_users, 'usesr1', '11111')