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


def password_verification(login, password):         # итог: константная
    if dict_obj[login][0] == password:              # константная
        return True                                 # константная
    return False                                    # константная


def active_verification(login):                     # итог: константная
    if dict_obj[login][1]:                          # константная
        return True                                 # константная
    return False                                    # константная


# Вариант-1
def authentification_1(login, password):                                              # итог: константная
    if dict_obj.get(login):                                                         # константная
        if password_verification(login, password) and active_verification(login):   # константная
            return 'Success!'                                                       # константная
        elif not password_verification(login, password):                            # константная
            return 'Incorrect password'                                             # константная
        elif not active_verification(login):                                        # константная
            return 'Please, complete the activation'                                # константная
    return 'User doesn\'t exist'                                                    # константная


# Вариант-2
def authentification_2(login, password):                                                  # итог: линейная
    for key in dict_obj.keys():                                                         # линейная
        if key == login:                                                                # константная
            if password_verification(login, password) and active_verification(login):   # константная
                return 'Success!'                                                       # константная
            elif not password_verification(login, password):                            # константная
                return 'Incorrect password'                                             # константная
            elif not active_verification(login):                                        # константная
                return 'Please, complete the activation'                                # константная
    return 'User doesn\'t exist'                                                        # константная
