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


# Общая сложность 0(n)
def authorization_f(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return 'Welcome! Access to the resource is provided'
            elif value['password'] == user_password and not users[user_name]['activation']:
                return 'The account is not active! Complete the activation'
            elif value['password'] != user_password:
                return 'The password is incorrect!'
            else:
                return 'This user does not exist'


# Общая сложность 0(1)
def authorization_s(users, user_name, user_password):
    if users[user_name]['password'] == user_password and users[user_name]['activation']:
        return 'Welcome! Access to the resource is provided'
    elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
        return 'The account is not active! Complete the activation'
    elif users[user_name]['password'] != user_password:
        return 'The password is incorrect!'
    else:
        return 'This user does not exist'

#оба решения было взято с вашей презентации домашнего задания
