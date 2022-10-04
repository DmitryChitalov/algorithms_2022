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

users = {'john2015': {'password': '235y6hugr',
                      'activation': False},
         'LaylaGreenfield@': {'password': '235fhje',
                              'activation': False},
         'Someuser123': {'password': 'shjty12kl',
                         'activation': True},
         'spamaccont': {'password': 'spamspam',
                        'activation': False}}


def verification(username, password):
    """
    :Сложность: O(1)
    """
    user_info = users.get(username)  # O(1)
    if user_info:
        check_password = user_info.get('password')  # O(1)
        activation = user_info.get('activation')  # O(1)
        if check_password == password and activation:  # O(1)
            return 'Access granted'  # O(1)
        elif check_password == password and not activation:  # O(1)
            return 'Please complete activation'  # O(1)
        else:
            return "Wrong Password"  # O(1)
    else:
        return "User Not Found"  # O(1)


def verification_2(username, password):
    """
    Сложность O(n)
    """
    user_pass = None
    password_pass = None
    activation_pass = None
    for k in users.keys():  # O(n)

        if k == username:
            user_pass = True  # O(1)
    if user_pass:
        for v in users[username].values():  # O(n)
            password_pass = True if v == password else password_pass  # O(1)
            activation_pass = True if v == True else activation_pass  # O(1)

        if password_pass and activation_pass:
            return 'Access granted'  # O(1)
        elif password_pass:
            return 'Please complete activation'  # O(1)
        else:
            return "Wrong Password"  # O(1)

    else:
        return "User Not Found"  # O(1)


"""
Вывод 
первое решение лучше нету бессмысленных циклов
"""

if __name__ == "__main__":
    # func 1
    for person in users:
        print(verification(person, users[person]['password']))
    print(verification('Wrong', 'False'))
    print(verification('john2015', "Wrong password"))
    # func 2
    for person in users:
        print(verification_2(person, users[person]['password']))
    print(verification_2('Wrong', 'False'))
    print(verification_2('john2015', "Wrong password"))
