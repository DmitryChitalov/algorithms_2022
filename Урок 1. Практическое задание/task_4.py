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

autentification = {
    'Batman': ('Whereisth#trigger?', True),
    'Jack': ('fghbjnm,mknjh5678212', True),
    'Hatman': ('Wouldy0ulik#sometea?', True),
    'Paule': ('cvbnm,lk45678uhn', True),
    'Raule': ('Cheeese456789kjhg!', False),
    'T1000': ('Illbback!', False)
}

"""First decision"""


def check_autentification_1(authent_dict: dict, login: str, password: str):
    """Функция принимает в себя словарь, логин и пароль.
    Проверяет вхождение логина в ключи словаря. В случае успеха сравнивает пароль и проверяет атктивность аккаунта
    И возвращает инфомрационное сообщение"""
    if login in [x for x in authent_dict.keys()]:  # Перебор O(N)
        if password == authent_dict[login][0]:  # Сравнение элемента O(1)
            if authent_dict[login][1] is True:  # Сравнение элемента O(1)
                return f'Success! "{login}", welcome back!'  # O(1)
            else:
                return f'We truly sorry,"{login}", but it seems that your account is not active! ' \
                       f'Would you like us to send activation letter? yes/no'  # O(1)
        return f'Wrong password for "{login}"'  # O(1)
    return f'No such account with name "{login}"'  # O(1)


# print(check_autentification_1(autentification, 'Hatman', 'Wouldy0ulik#sometea?'))
# print()
# print(check_autentification_1(autentification, 'T1000', 'Illbback!'))
# print()
# print(check_autentification_1(autentification, 'Batman', 'Wouldy0ulik#sometea?'))
# print()
# print(check_autentification_1(autentification, 'Gremlin', 'Needsomefood!!!!!!!'))
# print()


"""Second decision"""


autentification_2 = [
                    ['Batman', 'Whereisth#trigger?', True],
                    ['Jack', 'fghbjnm,mknjh5678212', True],
                    ['Hatman', 'Wouldy0ulik#sometea?', True],
                    ['Paule', 'cvbnm,lk45678uhn', True],
                    ['Raule', 'Cheeese456789kjhg!', False],
                    ['T1000', 'Illbback!', False]
                ]


def check_autentification_2(authent_list: list, login: str, password: str):
    """
    Функция принимает в себя вложенный список, логин и пароль.
    Сравнивает первую букву логина с средней буквой первого элемента в списке. Сокращает список на половину -1 элемент.
    Проверяет вхождение логина в list comprehension из первых значений вложенного списка если их пароль соответствует

    PS: Тут с идеями плохо и реализация кошмарная. Рубить список пополам рисковано.
    Хватило только фантазии частично ускорить процесс для случаев когда логин скорее всего есть в списке
    и мы может ускорить процесс сортировкой списка и обрезав его половину. Но это далеко не бинарный поиск"""
    sort_list = sorted(authent_list)  # Сортировка O(log N) #Присвоение O(1)
    half_letter = (authent_list[len(sort_list) // 2][0][0]).lower()  # Срез O(b-a)
    if login[0].lower() > half_letter:  # Сравнение элемента O(1)
        authent_list = sort_list[(len(sort_list) // 2)+1:]  # Срез O(b-a)
    else:
        authent_list = sort_list[:(len(sort_list) // 2)+1]  # Срез O(b-a)
    if login in [x[0] for x in authent_list if password in x and x[2] is True]:  # Перебор O(2N)
        return f'Success! "{login}", welcome back!'  # O(1)
    elif login in [x[0] for x in authent_list if password in x and x[2] is False]:  # Перебор O(2N)
        return f'We truly sorry,"{login}", but it seems that your account is not active! ' \
               f'Would you like us to send activation letter? yes/no'  # O(1)
    else:
        return f'Login "{login}" with such password not founded'  # O(1)


print(check_autentification_2(autentification_2, 'Paule', 'cvbnm,lk45678uhn'))
print(check_autentification_2(autentification_2, 'gremlin', 'Needsomefood!!!!!!!'))
