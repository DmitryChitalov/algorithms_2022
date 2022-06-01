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
users = [
    {'login' : 'Boris', 'password': 'qwer', 'activeted': True},
    {'login' : 'Andrew', 'password': 'asdf', 'activeted': False},
    {'login' : 'Victor', 'password': 'zxcv', 'activeted': True},
    {'login' : 'Irina', 'password': '1234', 'activeted': False}
    ]

# Для функции O(N)
def get_user(user_dict):
    for k, v in user_dict.items(): #O(N)
        if k == 'activeted':       #O(1)
            if not v:              #O(1)
                i = int(input('%s пожалуйста активируйте учетную запись (нажмите 1 - для активации)' % user_dict.get('login'))) #O(1)
                if i == 1:         #O(1)
                    print('active')
                    user_dict['activeted'] = True #O(1)
                else:
                    print('Активация не пройдена')
            else:
                print('{}, Ваша учетка активирована'.format(user_dict.get('login'))) #O(1)

# Общая O(N**2)
for user_dict in users: #O(N)
    get_user(user_dict) #O(N)

print(users)

# второй вариант

users_passw = {'Boris': 'qwer', 'Andrew': 'asdf', 'Victor': 'zxcv', 'Irina': '1234'}
users_activ = {'Boris': True, 'Andrew': False, 'Victor': True, 'Irina': False}

# Общая O(N)
for k in users_passw.keys():    #O(N)
    if not users_activ[k]:      #O(1)
        i = int(input('%s пожалуйста активируйте учетную запись (нажмите 1 - для активации)' % k))
        if i == 1:
            print('active')
            users_activ[k] = True #O(1)
        else:
            print('Активация не пройдена')
    else:
        print('{}, Ваша учетная запись активирована'.format(k))


"""
Второй вариант предпочтительнее, т.к. не проходит по списку
"""