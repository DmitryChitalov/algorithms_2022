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
users = {
    'Pam': ['1234', True], 'Sam': ['4321', False], 'Tim': ['a234', True],
    'Joe': ['b234', True], 'Ann': ['111', False], 'Suzy': ['c234', False]
}


def activation(name):                                       # O(1)
    answer = input('not active profile. activate?(y/n):')   # O(1)
    if answer == 'y':                                       # O(1)
        users[name][1] = True                               # O(1)
        print('activated')                                  # O(1)
    else:                                                   #
        print('not activated access forbidden')             # O(1)


def check_passwd(name):                                                    # O(1)
    passwd = input('password: ')                                           # O(1)
    if users[name][0] == passwd:                                           # O(1)
        print(f'success. user {name} - activation is {users[name][1]}')    # O(1)
    else:                                                                  #
        print('wrong password')                                            # O(1)


def user_login_fst(name):                           #
    if name in users and users[name][1] is False:   # O(n)
        activation(name)                            # O(1)
    else:                                           #
        print('active profile')                     #
    if users[name][1]:                              # O(1)
        check_passwd(name)                          # 0(1)
    else:                                           #
        pass                                        # O(1)


def passwd_check_snd(name):                         # O(n^2)
    u_passwd = input('password:')                   # O(1)
    for k, v in users.items():                      # O(n)
        if k == name:                               # O(1)
            for el in v:                            # O(n)
                if el == u_passwd:                  # O(1)
                    print(f'success. user {name} - activation is {users[name][1]}')     # O(1)
                    break                           # O(1)
                else:                               #
                    print('wrong password')         # O(1)
                    break                           # O(1)


def user_login_snd(name):                                                   # O(n^3)
    for k in users:                                                         # O(n)
        if k == name:                                                       # O(1)
            if users[name][1]:                                              # O(1)
                print('active profile')                                     # O(1)
                passwd_check_snd(name)                                      # O(n^2)
            else:                                                           #
                answer = input('not active profile. activate?(y/n):')       # O(1)
                if answer == 'y':                                           # O(1)
                    u_data = users.pop(name)                                # O(1)
                    u_data[1] = True                                        # O(1)
                    users.update({name: u_data})                            # O(1)
                    print('activated')                                      # O(1)
                    passwd_check_snd(name)                                  # O(n^2)
                else:                                                       #
                    print(f'not activated access forbidden')                # O(1)
            return                                                          # O(1)


# Проверка решений:
# user_login_fst('Pam')
# user_login_snd('Ann')

'''
Вывод: если задача позволяет использовать простое решение, нужно использовать его. 
Если можно обойтись без цикла, тем более без вложенного цикла - лучше их не использовать
с точки зрения O. 
'''