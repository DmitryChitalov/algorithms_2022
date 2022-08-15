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
    'T1000': ('Illbback!', False),
}

"""First decision"""


def check_autentification_1(authent_dict, login: str, password: str):
    if login in [x for x in authent_dict.keys()]:
        if password == authent_dict[login][0]:
            if authent_dict[login][1] == True:
                return f'Success! "{login}", welcome back!'
            else:
                return f'We truly sorry,"{login}", but it seems that your account is not active! ' \
                       f'Would you like us to send activation letter? yes/no'
        return f'Wrong password for "{login}"'
    return f'No such account with name "{login}"'

"""
print(check_autentification_1(autentification, 'Hatman', 'Wouldy0ulik#sometea?'))
print()
print(check_autentification_1(autentification, 'T1000', 'Illbback!'))
print()
print(check_autentification_1(autentification, 'Batman', 'Wouldy0ulik#sometea?'))
print()
print(check_autentification_1(autentification, 'Gremlin', 'Needsomefood!!!!!!!'))
print()
"""


def check_autentification_2(authent_dict: dict, login: str, password: str):
    """Записить с бинарной сортировкой"""
    #            return f'We truly sorry,"{login}", but it seems that your account is not active! ' \
    #                   f'Would you like us to send activation letter? yes/no'
    #    return f'Wrong password for "{login}"'
    #return f'No such account with name "{login}"'


check_autentification_2(autentification, 'gremlin', 'Needsomefood!!!!!!!')