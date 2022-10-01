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


def auth_user(id, passw, users):                                #O(1)
    status = ''                                                 #O(1)

    if id not in users.keys():                                  #O(1)
        status = 'Пользователя не существует'                   #O(1)
    elif passw != users[id][0]:                                 #O(1)
        status = 'Пароль введен неверно'                        #O(1)
    elif users[id][1] == False:                                 #O(1)
        status = 'Учетная запись не активирована'                #O(1)
        to_activate = int(input('Введите 1 - чтобы активировать учетную запись, 0 - для выхода: '))     #O(1)
        if to_activate:                                         #O(1)
            users[id][1] = True                                 #O(1)
            status = 'Учетная запись успешно активирована'      #O(1)
    else:
        status = 'Вы успешно вошли в систему'
    return status, users                            #O(1)


users = {                                           #O(1)
    'Roman123': ['us123', True],
    'Dmitry333': ['su098', True],
    'Victor544': ['ssdf', False],
    'Alex23': ['werf65', True],
    'Nikolai65': ['soie25', False]
}

print(users)                                        #O(1)
id_inp = input('Введите id пользователя: ')         #O(1)
passw_inp = input('Введите пароль: ')               #O(1)
print(auth_user(id_inp, passw_inp, users)[0])       #O(1)

# print(users)                                        #O(1)

id_inp = input('Введите id пользователя: ')         #O(1)
passw_inp = input('Введите пароль: ')               #O(1)
print(auth_user(id_inp, passw_inp, users)[0])       #O(3)
print(users)                                        #O(1)