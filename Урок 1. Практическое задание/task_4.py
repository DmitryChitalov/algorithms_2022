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

user_dict = {}
user_1 = {
          'password': 'password_1',
          'activated': True}
user_2 = {
          'password': 'password_2',
          'activated': True}
user_3 = {
          'password': 'password_3',
          'activated': False}
user_dict['user_1'] = user_1
user_dict['user_2'] = user_2
user_dict['user_3'] = user_3

print(user_dict)


def check_1(log, passwd):
    """
    Сложность: О(1)
    """
    if user_dict.get(log):                                        # O(1)
        if user_dict[log]['password'] == passwd:                  # O(1)
            if user_dict[log]['activated']:                       # O(1)
                return 'Вход выполнен'                            # O(1)
            return 'Необходимо активировать учетную запись'       # O(1)
        return 'Incorrect login and/or password'                  # O(1)
    return "Пользователь с таким именем не зарегистрирован"       # O(1)


def check_2(log, passwd):
    """
    Сложность: О(n)
    """
    for key, value in user_dict.items():                           # O(n)
        if key == log:                                             # O(1)
            if value['password'] == passwd:                        # O(1)
                if value['activated']:                             # O(1)
                    return 'Вход выполнен'                         # O(1)
                return 'Необходимо активировать учетную запись'    # O(1)
            return 'Incorrect login and/or password'               # O(1)
    return 'Пользователь с таким именем не зарегистрирован'        # O(1)


login = input("Login: ")
password = input("Password: ")
print(check_1(login, password))
print(check_2(login, password))
