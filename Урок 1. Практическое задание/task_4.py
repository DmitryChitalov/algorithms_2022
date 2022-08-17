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


def authentication_0(db_users, current_user):
    """
    Принимает словарь с заведенными учетными записями, список с данными пользователя и сравнивает данные.
    В случае успешной аутентификации возвращает True
    В случае несовпадения данных возвращает соответствующее исключение.
    @param db_users: Dictionary
    @param current_user: List
    @return: Boolean or ValueError
    Сложность: O(n) - Линейная.
    """
    _user_name, _user_hash = current_user[0], current_user[1]  # O(1)
    password_error = ValueError('Неверный пароль.')  # O(1)
    login_error = ValueError('Учетная запись не найдена.')  # O(1)
    confirm_error = ValueError(f'{_user_name}, вам необходимо подтвердить данные вашей учетной записи.')  # O(1)
    for db_user in db_users.values():  # O(n)
        if db_user[0] == _user_name:  # O(1)
            if db_user[1] == _user_hash:  # O(1)
                return True if db_user[2] else confirm_error
            else:  # O(1)
                return password_error  # O(1)
    else:  # O(1)
        return login_error  # O(1)


def authentication_1(db_users, current_user):
    """
    Принимает словарь с заведенными учетными записями, список с данными пользователя и сравнивает данные.
    В случае успешной аутентификации возвращает True
    В случае несовпадения данных возвращает соответствующее исключение.
    @param db_users: Dictionary
    @param current_user: List
    @return: Boolean or ValueError
    Сложность: O(n**2) - Квадратичная
    """
    _user_name, _user_hash = current_user[0], current_user[1]  # O(1)
    for db_user in db_users.values():  # O(n)
        for user_data in db_user:  # O(n)
            if user_data == _user_name:  # O(1)
                if db_user[1] == _user_hash:  # O(1)
                    return True if db_user[2] else ValueError(
                        f'{_user_name}, вам необходимо подтвердить данные вашей учетной записи.')  # O(1)
                return ValueError('Неверный пароль.')  # O(1)
    return ValueError('Учетная запись не найдена.')  # O(1)


if __name__ == '__main__':
    users = {
        1: ['br14', '827ccb0eea8a706c4c34a16891f84e7b', True],
        2: ['tombs2', 'ea2b2676c28c0db26d39331a336c6b92', True],
        3: ['cow3', '9bc65c2abec141778ffaa729489f3e87', False],
        4: ['OtrSetNpul', 'cdcd267dd9829fbb9070142d231d16b0', True],
        5: ['Sigon32', 'a67e565b11cd18f7a922b58f5476b569', True],
        6: ['hesoyam', 'cafc7170ed01c2f5c972cac7cde6e932', False]
    }

    our_user = ['hesoyam', 'cafc7170ed01c2f5c972cac7cde6e932']  # предполагается что на вход идет уже хеш
    print(authentication_0(users, our_user))
    print(authentication_1(users, our_user))


# revision
def authentication_2(db_users, current_user, current_password):
    """
    Принимает словарь с заведенными учетными записями, id пользователя, пароль и сравнивает данные.
    В случае успешной аутентификации возвращает True
    @param db_users: Dictionary
    @param current_user: List
    @param current_password: String
    @return: ValueError
    Сложность: O(1) - Константная
    """
    password_error = ValueError('Неверный пароль.')  # O(1)
    login_error = ValueError('Учетная запись не найдена.')  # O(1)
    confirm_error = ValueError(
        f'{db_users[current_user][0]}, вам необходимо подтвердить данные вашей учетной записи.')  # O(1)
    if db_users.get(current_user):  # O(1)
        if db_users[current_user][1] == current_password:  # O(1)
            return True if db_users[current_user][2] else confirm_error  # O(1)
        else:
            return password_error  # O(1)
    else:
        return login_error  # O(1)


if __name__ == '__main__':
    our_user_2, user_2_password = 6, 'cafc7170ed01c2f5c972cac7cde6e932'
    print(authentication_2(users, our_user_2, user_2_password))
