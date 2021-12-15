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


ВЫВОДЫ:
По критеирю "удобство использования" на мой взгляд самое эффективное первое решение,
т.к. оно усточиво в неверному вводу

"""


# O(n)
from pip._internal.network.session import user_agent
from setuptools.package_index import user_agent


def grant_access1(user_name, vault):
    """
    :param user_name: user name
    :param vault: password storage
    :return: true if granted, otherwise false
    """
    user_info = vault.get(user_name)
    if not user_info:
        print('Пользователь не найден.')
        return False

    password = input('Введите пароль:')
    if password != user_info['password']:
        print('Пароль неверный')
        return False

    if not user_info['active']:
        answer_yes = ['yes', 'y', 'yep', 'д', 'да']
        answer_no = ['no', 'n', 'not', 'н', 'нет']
        while True:
            action = input('Пользователь не активирован, активировать сейчас? (д/н)')
            if action in answer_no:
                print('Доступ запрещен, активация обязательна')
                return False
            if action in answer_yes:
                user_info['active'] = True
                print('Активация успешна')
                break

    return True


# O(1)
def grant_access2(user_name, vault):
    """
    :param user_name: user name
    :param vault: password storage
    :return: true if granted, otherwise false
    """
    user_info = vault.get(user_name)
    if not user_info:
        print('Пользователь не найден.')
        return False

    password = input('Введите пароль:')
    if password != user_info['password']:
        print('Пароль неверный')
        return False

    if not user_info['active']:
        answer_yes = ['yes', 'y', 'yep', 'д', 'да']
        answer_no = ['no', 'n', 'not', 'н', 'нет']
        action = input('Пользователь не активирован, активировать сейчас? (д/н)')
        if action in answer_no:
            print('Доступ запрещен, активация обязательна')
            return False
        if action in answer_yes:
            user_info['active'] = True
            print('Активация успешна')
            return True

        print('Ответ не распознан, доступ запрещен')
        return False

    return True


if __name__ == "__main__":

    vault = {
        'user_name1': {'password': '1', 'active': True},
        'user_name2': {'password': '2', 'active': False}
    }

    # Пример использования

    print('Вариант 1', end='\n\n')

    user_name = "user_name1"
    print('Пользователь:', user_name)
    print(grant_access1(user_name, vault))
    user_name = "user_name2"
    print('Пользователь:', user_name)
    print(grant_access1(user_name, vault))
    user_name = "user_name3"
    print('Пользователь:', user_name)
    print(grant_access1(user_name, vault))

    print()
    print('Вариант 2', end='\n\n')
    user_name = "user_name1"
    print('Пользователь:', user_name)
    print(grant_access2(user_name, vault))
    user_name = "user_name2"
    print('Пользователь:', user_name)
    print(grant_access2(user_name, vault))
    user_name = "user_name3"
    print('Пользователь:', user_name)
    print(grant_access2(user_name, vault))
