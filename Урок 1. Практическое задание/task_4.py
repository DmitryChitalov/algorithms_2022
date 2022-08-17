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




our_users = {'user1': ['12345', True], 'user2': ['1234', False]}


def prove_user(username, password):                         # O(1)
    if our_users.get(username):                             # O(1)
        if password == our_users[username][0]:              # O(1)
            if our_users[username][1]:                      # O(1)
                print('Access granted')                     # O(1)
            else:
                print('Activate your account')              # O(1)
        else:
            print('Password is not correct')                # O(1)
    else:
        print('This account doesn\'t exist')                # O(1)

prove_user('user1', '12345')
prove_user('user4', '12345')
prove_user('user2', '1234')


our_users_list = [['user1', '12345', True], ['user2', '1234', False]]


def prove_user2(username, password, userlist):                         # O(n)
    for user in userlist:                                              # O(n)
        if user[0] == username and user[1] == password:                # O(1)
            if user[2]:                                                # O(1)
                print('Access granted')                                # O(1)
                break
            else:
                print('Activate your account')                         # O(1)
                break
    else:
        print('Usernsme or password incorrect')                        # O(1)

print('-----')
prove_user2('user1', '12345', our_users_list)
prove_user2('user4', '12345', our_users_list)
prove_user2('user2', '1234', our_users_list)


"""

Вывод. 
Во втором решении используется цикл, перебирающий все элементы списка. 
Это увеличивает алгоритмическую сложность до линейной. 
Поиск по ключу в словаре имеет константную сложность.
Первое решение эффективнее, так как константная сложность ниже линейной. 

"""