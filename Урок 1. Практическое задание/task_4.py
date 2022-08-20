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


# сложность: O(n^2)
def registration(dct):
    login = input('Логин:')
    password = int(input('Пароль:'))
    if login in dct.keys() and password == dct[login]['password'] and dct[login]['act'] == 'activated':
        print('Вы вошли успешно')
    elif login not in dct.keys():
        ask = input('Такого пользователя не существует. хотите зарегистрироваться?')
        if ask == 'yes':
            login = input('Логин:')
            password = int(input('Пароль:'))
            dic = {'password': password, 'act': 'activate'}
            dct[login] = dic
            print('Вы зарегестрировались!')
        else:
            print('Без активации вы не сможете войти в учетную запись!')
    elif login in dct.keys() and dct[login]['password'] == password and dct[login]['act'] != 'activated':
        ask = input('Ваш аккаунт не активирован.Хотите активировать?')
        if ask == 'yes':
            dct[login]['act'] = 'activate'
            print('Вы успешно акивировали аккаунт')
        else:
            print('Без активации вы не сможете войти в учетную запись!')


users = {'Ivan': {'password': 5243, 'act': 'activated'},
         'Misha48': {'password': 76549, 'act': 'not activated'},
         'Alex': {'password': 34976, 'act': 'activated'}}

print(registration(users))


# константная
def authorization(users, user_name, user_password):
    if users.get(user_name):                                            # O(1) - Константная
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:                     # O(1) - Константная
            return "Здравствуйте! Вы допущены к ресурсу"
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:                 # O(1) - Константная
            return "Учетная запись не активна! Пройдите активацию!"     # O(1) - Константная
        elif users[user_name]['password'] != user_password:             # O(1) - Константная
            return "Пароль не верный"                                   # O(1) - Константная
    else:
        return "Данного пользователя не существует"


my_users = {'Ivan': {'password': '1234', 'activation': True},
            'Misha': {'password': 'qwert', 'activation': False},
            'Dima': {'password': '1453', 'activation': True},
            'Anton': {'password': '2407', 'activation': False}}

print(authorization(my_users, 'Ivan', '1234'))
print(authorization(my_users, 'user6', '1111'))
