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

users = {'Stepan': {'password': 'qwerty123', 'is_activated': False},
         'Alice': {'password': 'jnsSD!icvh3334', 'is_activated': True},
         'Bob': {'password': '%&DSDB*3g2', 'is_activated': True},
         'Gulbakhtim': {'password': '_)*jdn27', 'is_activated': False},
         'Satoshi': {'password': ':Jdjbdfy%^gs2', 'is_activated': True}}


def auth_a(login):  # O(1)
    if users[login]['is_activated']:
        return f'You have successfully logged in as {login}'
    else:
        print(f'Your account {login} is not activated yet')
        activation = input('Do you want to activate it? Y/N: ').lower()
        if activation == 'y':
            users[login]['is_activated'] = True
            return f'Account {login} is successfully activated'
        else:
            return f'okay :('

def auth_b(login): # O(n)
    for k, v in users.items():
        if login == k and v['is_activated'] == False:
            print(f'Your account {login} is not activated yet')
            activation = input('Do you want to activate it? Y/N: ').lower()
            if activation == 'y':
                users[login]['is_activated'] = True
                return f'Account {login} is successfully activated'
            else:
                return f'okay :('
        else:
            return f'You have successfully logged in as {login}'


print(auth_a('Stepan'))
print('*' * 40)
print(auth_a('Alice'))
print('*' * 40)
print(auth_b('Stepan'))
print('*' * 40)
print(auth_b('Alice'))

