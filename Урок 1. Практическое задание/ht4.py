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

my_dict = {
    'e_chernykh': ['1234', True],
    'Kate': ['0987654321', True],
    'Max': ['qwerty', False]
}

def check_1(web_dict, login, password): # общая сложность O(N)
    if login not in web_dict: # O(N)
        return print('Неверный логин!') # O(1)
    elif login in web_dict and web_dict[login][0] != password: # O(N)
        return print('Неверный пароль!') # O(1)
    elif login in web_dict and web_dict[login][0] == password and web_dict[login][1] == True: # O(N)
        return print('Верификация пройдена!') # O(1)
    elif login in web_dict and web_dict[login][0] == password and web_dict[login][1] == False: # O(N)
        return print('Необходимо пройти аутентификацию') # O(1)

my_login = input('Введите логин: ')
my_password = input('Введите пароль: ')
check_1(my_dict, my_login, my_password)

def check_2(web_dict, login, password): # общая сложность O(1)
    if web_dict.get(login): # O(1)
        if web_dict[login][0] == password and web_dict[login][1] == True: # O(1)
            return print('Верификация пройдена!')  # O(1)
        elif web_dict[login][0] == password and web_dict[login][1] == False: # O(1)
            return print('Необходимо пройти аутентификацию')  # O(1)
        elif web_dict[login][0] != password: # O(1)
            return print('Неверный пароль!')  # O(1)
    else: # O(1)
        return print('Неверный логин!')  # O(1)

my_login = input('Введите логин: ')
my_password = input('Введите пароль: ')
check_2(my_dict, my_login, my_password)