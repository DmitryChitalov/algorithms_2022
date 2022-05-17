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


def check_1(user, password, users: dict[str, tuple[str, bool]]) -> bool:
    # Сложность O(1)
    authentification = users.get(user)  # O(1)
    if authentification:  # O(1)
        if (password == authentification[0]):  # O(1)
            if authentification[1]:  # O(1)
                print('Вход выполнен')
                return True  # O(1)
            else:
                print('Ваша учётная запись неактивна')
                return False  # O(1)
    print('Неверный логин/пароль')
    return False  # O(1)


def check_n(user, password, users: dict[str, tuple[str, bool]]) -> bool:
    #Сложность O(N)
    for user_s in users: # O(N)
        if user == user_s: # O(1)
            if password == users[user_s][0]: # O(1)
                if users[user_s][1]: # O(1)
                    print('Вход выполнен')
                    return True  # O(1)
                else:
                    print('Ваша учётная запись неактивна')
                    return False  # O(1)
    print('Неверный логин/пароль')
    return False  # O(1)


users = {
    'admin': ('pass', True),
    'user_1': ('pass1', False),
    'user_2': ('pass1', True)
}
print(check_1('user_1', 'pass1', users))
print(check_1('admin', 'pass', users))
print(check_n('user_1', 'pass1', users))
print(check_n('admin', 'pass', users))
