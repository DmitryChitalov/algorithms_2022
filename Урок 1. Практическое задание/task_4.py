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



def authorization_one(users, user_name, user_password):
    """
    Проверка логина и пароля пользователя, а также активирована ли его запись
    сложность O(n)
    :param users: словарь пользователей
    :param user_name: введенное имя пользователя
    :param user_password: введенный пароль
    :return: строка в зависимости от логикиги нахождения пользователя в словаре
    """
    if user_name in users:  # O(n)
        for key, value in users.items():  # O(n)
            if key == user_name:  # O(1)
                if value['password'] == user_password:  # O(1)
                    if value['activation']:  # O(1)
                        return 'Добро пожаловать в систему'  # O(1)
                    else:
                        return 'Ваша учетная запись не активирована, пройдите активацию'  # O(1)
                else:
                    return 'Вы ввели не правильный пароль'  # O(1)
    else:
        return f'Пользователя {user_name} нет в системе'  # O(1)



def authorization_two(users, user_name, user_password):
    """
    Проверка логина и пароля пользователя, а также активирована ли его запись
    сложность O(1)
    :param users: словарь пользователей
    :param user_name: введенное имя пользователя
    :param user_password: введенный пароль
    :return: строка в зависимости от логикиги нахождения пользователя в словаре
    """
    if users.get(user_name) != None:  # O(1)
        if user_password == users[user_name]['password']:  # O(1)
            if users[user_name]['activation']:  # O(1)
                return 'Добро пожаловать в систему'  # O(1)
            else:
                return 'Ваша учетная запись не активирована, пройдите активацию'  # O(1)
        else:
            return 'Вы ввели не правильный пароль'  # O(1)

    else:
        return f'Пользователя {user_name} нет в системе'  # O(1)



if __name__ == '__main__':
    my_users = {'vasya': {'password': '123456', 'activation': False},
                'petya': {'password': '654321', 'activation': True},
                'sergey': {'password': 'qwerty', 'activation': True},
                'sasha': {'password': 'retry', 'activation': True}
                }

    print(authorization_one(my_users, 'user', '123456'))
    print(authorization_one(my_users, 'vasya', '123456'))
    print(authorization_one(my_users, 'sergey', 'fogot'))
    print(authorization_one(my_users, 'sergey', 'qwerty'))



    print(authorization_two(my_users, 'user', '123456'))
    print(authorization_two(my_users, 'vasya', '123456'))
    print(authorization_two(my_users, 'sergey', 'fogot'))
    print(authorization_two(my_users, 'sergey', 'qwerty'))

    """
       Вторая функцмя эффективнее по сравнению сложностей, так как у нее сложность O(1), 
       потому что в отличие от первой она не использует цикл и проверку на вхождение ключа в словарь
       """
