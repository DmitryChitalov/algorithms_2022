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

user_pas_dict = {'ivan': '123', 'nick': 'qwe', 'lila': '111'}
user_activ_dict = {'ivan': 1, 'nick': 0, 'lila': 1}


# Решение 1.  Сложность O(1)


def auth(user, paswd):
    if user in user_pas_dict and paswd == user_pas_dict[user]:  # O(1)
        if user_activ_dict[user] == 1:  # O(1)
            print(f'Welcome, {user}')  # O(1)
        else:
            print(f'{user}, please activate your profile for login')  # O(1)
    else:
        print('Unknown user or wrong password')  # O(1)
    return  # O(1)


auth('ivan', '123')
auth('nick', 'qwe')
auth('lila', '123')

print("---------------------------")


# Решение 2.  Сложность O(N)


def auth(user, paswd):
    log = 0  # O(1)
    for k, v in user_pas_dict.items():  # O(N)
        if user == k and paswd == v:  # O(1)
            if user_activ_dict[user] == 1:  # O(1)
                print(f'Welcome, {user}')  # O(1)
                log = 1  # O(1)
                break
            else:
                print(f'{user}, please activate your profile for login')  # O(1)
                log = 1  # O(1)
                break
    if log == 0:  # O(1)
        print('Unknown user or wrong password')  # O(1)
    return  # O(1)


auth('ivan', '123')
auth('nick', 'qwe')
auth('lila', '123')

# Первое решение эффективнее по скорости выполнения, а также по количеству кода
