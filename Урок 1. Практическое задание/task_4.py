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

users = [('Nik', '1458rtfy', True),
         ('PyPit', '18trfy', True),
         ('Den', 'TTggPP15', True),
         ('Ann', 'qwerty12', False),
         ('Kolia', 'qwerqwer', True),
         ]


def data_valid_1(data_base: list, data: tuple):
    '''
    Функция принимает список данных учетных записей и кортеж введенных пользователем данных и проверяет их соответствие
    Ничего не возвращает, печатает результат
    Сложность: O(n)        T(n) = n(1+1+1+1+3+4+1)=12n
    :param data_base: list
    :param data: tuple
    :return: None
    '''
    for el in data_base:  # O(n)
        if el[0] == data[0] and el[1] == data[1] and el[2]:  # O(1)
            return 3  # O(1)
        elif el[0] == data[0] and el[1] != data[1]:  # O(1)
            return 4  # O(1)
        elif el[0] == data[0] and el[1] == data[1] and not el[2]:  # O(1)
            return 2  # O(1)
    return 1  # O(1)


def data_valid_2(data_base: list, data: tuple):
    '''
    Функция принимает список данных учетных записей и кортеж введенных пользователем данных и проверяет их соответствие
    Ничего не возвращает, печатает результат
    Сложность: O(n)          T(n) = 1+1+1+n(1+1+1)+n+n+1+1+1 = 5n +6

    :param data_base: list
    :param data: tuple
    :return: None
    '''
    login_list = []  # O(1)
    password_list = []  # O(1)
    activation_list = []  # O(1)
    for el in data_base:  # O(n)
        login_list.append(el[0])  # O(1)
        password_list.append(el[1])  # O(1)
        activation_list.append(el[2])  # O(1)
    if data[0] not in login_list:  # O(n)
        return 1
    idx = login_list.index(data[0])  # O(n)
    if data[1] != password_list[idx]:  # O(1)
        return 4  # O(1)
    elif not activation_list[idx]:  # O(1)
        return 2
    else:
        return 3  # O(1)


def data_valid_3(data_base: list, data: tuple):
    '''
    Функция принимает список данных учетных записей и кортеж введенных пользователем данных и проверяет их соответствие
    Ничего не возвращает, печатает результат
    Сложность: O(n^2)          T(n) = n(1+n+1)+1+1+1+1+1 = n^2+2n+5

    :param data_base: list
    :param data: tuple
    :return: None
    '''

    while len(users) != 0:  # O(n)
        el = users.pop()  # O(1)
        if data[0] not in el:  # O(n)
            continue  # O(1)
        else:
            break  # O(1)
    if el[2]:  # O(1)
        return 3  # O(1)
    elif el[1] != data[1]:  # O(1)
        return 4  # O(1)
    else:
        return 2  # O(1)
    return 1  # O(1)


def log_in(n):
    '''
    Приниает от пользователя логин и пароль и возвращает кортеж
    :param n: int - номер функции для валидации
    :return: tuple

    Сложность: 0(1)
    '''
    login = input('LOGIN:')  # 0(1)
    password = input('PASSWORD:')  # 0(1)
    data = login, password  # 0(1)
    if n == 1:  # 0(1)
        x = data_valid_1(users, data)  # 0(1)
    elif n == 2:  # 0(1)
        x = data_valid_2(users, data)  # 0(1)
    elif n == 3:  # 0(1)
        x = data_valid_3(users, data)  # 0(1)
    if x == 1:  # 0(1)
        print(f'Пользователь {login} не зарегистрирован')  # 0(1)
    elif x == 2:  # 0(1)
        print(f'Учетная запись пользователя {login} не активирована. Желаете активировать?')  # 0(1)
    elif x == 3:  # 0(1)
        print(f'Пользователю {login} доступ открыт')  # 0(1)
    elif x == 4:  # 0(1)
        print(f'Неверный пароль')  # 0(1)


log_in(1)
log_in(2)
log_in(3)


# Алгоритмы 1 и 2 ф-ии по сложности линейные, 3 - квадратичный, он проигрывает по скорости
# По восприятию кода для меня проще 1 и 3.