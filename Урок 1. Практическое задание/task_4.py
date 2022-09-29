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


def access_1(my_dict):
    """Функция обеспечивает проверку возможности допуска пользователя к ресурсу.
    Решение 1:
    Задаем условие проверки данных о пользователе.
    Если оно выполняется, пользователь
    получает доступ к ресурсу.
    Сложность: O(1).
    """
    if my_dict['activation'] == 'True':  # O(1)
        return (f'User {my_dict["login"]} is admitted to the resource.')  # O(1)
    return (f'User {my_dict["login"]} is not allowed to access the resource. Get authenticated.')  # O(1)


user_1 = {'login': 'Nancy', 'pass': 123, 'activation': 'False'}
user_2 = {'login': 'Kim', 'pass': 456, 'activation': 'True'}

print(access_1(user_1))
print(access_1(user_2))


def access_2(my_dict):
    """Функция обеспечивает проверку возможности допуска
    пользователя к ресурсу.
    Решение 2:
    Просим пользователя ввести логин и пароль.
    Проверяем введёные пользователем данные.
    Если данные совпадают с информацией в словаре,
    пользователь получает доступ к ресурсу.
    Сложность: O(n).
    """
    for key, value in my_dict.items():  # O(n)
        login_user = input('Введите имя: ')
        password_user = int(input('Введите пароль: '))
        if key == login_user:  # O(1)
            if value['pass'] == password_user and value['activation'] == 'True':  # O(1)
                return (f'User {login_user} is admitted to the resource.')
            elif value['pass'] == password_user and value['activation'] != "True":  # O(1)
                return (f'User {login_user} is not allowed to access the resource. Get authenticated.')
            elif value['pass'] != password_user:  # O(1)
                return "Invalid password. Try again"
        return (f'User {login_user} is not found')  # O(1)


user_3 = {'Michael': {'pass': 789, 'activation': 'False'}}
user_4 = {'Larry': {'pass': 321, 'activation': 'True'}}

print(access_2(user_3))
print(access_2(user_4))

"""
Решение 1 эффективнее. Так как мы не производим итерацию словаря.
Так же у решения 1 темп роста количества операцй для произведения сортировки O(1), он меньше чем у решения №2 O(n).
"""