"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

USERS = {'user_1': {'user_login': 'tomilov.alex@gmail.com',
                    'user_password': 123,
                    'is_active': True},
         'user_2': {'user_login': 'ildar.gimadeev@mail.ru',
                    'user_password': 123,
                    'is_active': False}
         }


# вариант с разбора с использованием доступа по ключу (немного измененный вариант)
def user_check_1(users, user_name, user_login, user_password):
    """
    Функция проверки пользователя:
    сложность константная O(1)
    """
    if users.get(user_name):
        if users[user_name]['user_login'] == user_login \
                and users[user_name]['user_password'] == user_password \
                and users[user_name]['is_active']:
            return True, print('Добро пожаловать')
        elif users[user_name]['user_login'] == user_login \
                and users[user_name]['user_password'] == user_password \
                and not users[user_name]['is_active']:
            return False, print('Пользователь не активирован')
    return False, print('Проверьте логин или пароль')


if __name__ == '__main__':
    user_check_1(USERS, 'user_1', 'tomilov.alex@gmail.com', 123)
    user_check_1(USERS, 'user_2', 'ildar.gimadeev@mail.ru', 123)
    user_check_1(USERS, 'user_3', 'mikhail.adeev@mail.ru', 123)


# вариант с разбора с перебором значений (немного измененный вариант)
def user_check_1(users, user_name, user_login, user_password):
    """
    Функция проверки пользователя:
    сложность константная O(n)
    """
    for name, data in users.items():
        if user_name == user_name:
            if data['user_login'] == user_login \
                    and data['user_password'] == user_password \
                    and data['is_active']:
                return True, print('Добро пожаловать')
            elif data['user_login'] == user_login \
                    and data['user_password'] == user_password \
                    and not data['is_active']:
                return False, print('Пользователь не активирован')
    return False, print('Проверьте логин или пароль')


if __name__ == '__main__':
    user_check_1(USERS, 'user_1', 'tomilov.alex@gmail.com', 123)
    user_check_1(USERS, 'user_2', 'ildar.gimadeev@mail.ru', 123)
    user_check_1(USERS, 'user_3', 'mikhail.adeev@mail.ru', 123)
