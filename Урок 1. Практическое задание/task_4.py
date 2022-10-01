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

users = [
    {'Login': 'atkhnn', 'Password': '1230', 'is_activated': 'True'},
    {'Login': 'ektiv', 'Password': '8901', 'is_activated': 'True'},
    {'Login': 'cvtr', 'Password': '5678', 'is_activated': 'True'},
    {'Login': 'vikishow', 'Password': '2345', 'is_activated': 'False'},
    {'Login': 'wedro', 'Password': '7890', 'is_activated': 'False'},
    {'Login': 'orfil', 'Password': '4567', 'is_activated': 'True'},
    {'Login': 'kirabell', 'Password': '1234', 'is_activated': 'False'}
]

login = []
password = []
is_activated = []
for i in users:
    login.append(i['Login'])
    password.append(i['Password'])
    is_activated.append(i['is_activated'])

#Сложность: O(n)

def authentication(login, password):
    for i in users:                                                                    #O(n)
        if i.get('Login') == login:                                                    #O(1)
            if i.get('Password') == password:                                          #O(1)
                if i.get('is_activated') == 'True':                                    #O(1)
                    return f'Доступ разрешен'                                          #O(1)
                else:
                    return f'Ваш аккаунт не активирован. Хотите пройти активацию?'     #O(1)
            else:
                return f'Введите корректный пароль'                                    #O(1)

print(authentication(login[0], password[2]))

#Сложность: O(n^2)

def authentication_2(login, password):
    for i in login:                                                                                 #O(n)
        for t in password:                                                                          #O(n)
            if login.index(i) == password.index(t) and is_activated[login.index(i)] == 'True':      #O(1)
                return f'Доступ разрешен'                                                           #O(1)
            elif login.index(i) == password.index(t) and is_activated[login.index(i)] == 'False':   #O(1)
                return f'Ваш аккаунт не активирован. Хотите пройти активацию?'                      #O(1)
            elif login.index(i) != password.index(t):                                               #O(1)
                return f'Введите корректный пароль'                                                 #O(1)

print(authentication_2(login[3], password[3]))

#Вывод: эффективнее будет использовать первое решение, так как первое решение - линейная сложность, а второе - квадратичная
