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
При этом его учётка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from time import sleep

DATA = {'nikpick': [True, 'psdfj52'], 'picknik': [False, '238rheyf']}


# Solve 1
def log_in_1(login: str, password: str, data_users=None):
    """
    Функция аутентификации пользователя.
    Проверка существования логина, статус активации аккаунта, верность пароля
    в заданной базе данных пользователей

    Сложность: O(1)
    :param data_users:
    :param login:
    :param password:
    :return: None
    """
    if data_users is None:
        data_users = DATA
    while True:
        if DATA.get(login):  # O(1)
            if DATA.get(login)[0]:  # O(1)
                if DATA.get(login)[1] == password:  # O(1)
                    print(f'Welcome, {login}!')
                    break
                print('Wrong password!')
                user_input = input('Try again? [Yes: y/Y, No: other key]')
                if user_input in 'Yy':  # O(1)
                    DATA[login][0] = True  # O(1)
                    password = input('Your password: ')
                    continue
                print(f'Bye, {login}!')
                break
            print('Your account is not activated!')
            user_input = input('Do you want activate it? [Yes: y/Y, No: other key]')
            if user_input in 'Yy':  # O(1)
                DATA[login][0] = True  # O(1)
                print('Magic is going...')
                sleep(2)
                print(f'{login}, your account is activated!')
                continue
            print(f'Bye, {login}!')
            break
        print(f'Account with login {login} is not in data. Check the correctness of the login set')


# Solve 2
def log_in_2(login: str, password: str, data_users=None):
    """
    Функция аутентификации пользователя.
    Проверка существования логина, статус активации аккаунта, верность пароля
    в заданной базе данных пользователей

    Сложность: O(N)
    :param data_users:
    :param login:
    :param password:
    :return: None
    """
    if data_users is None:
        data_users = DATA
    for key, value in data_users.items():
        if key == login:
            if not value[0]:
                print('Your account is not activated!')
                user_input = input('Do you want activate it? [Yes: y/Y, No: other key]')
                if user_input in 'Yy':
                    data_users[login][0] = True
                    print('Magic is going...')
                    sleep(2)
                    print(f'{login}, your account is activated!')
                else:
                    print(f'Bye, {login}!')
                    break
            if value[1] != password:
                print('Wrong password!')
                user_input = input('Try again? [Yes: y/Y, No: other key]')
                if user_input in 'Yy':  # O(1)
                    DATA[login][0] = True  # O(1)
                    password = input('Your password: ')
                    continue
                else:
                    print(f'Bye, {login}!')
                    break
            print(f'Welcome, {login}!')
            break
    if login not in data_users.keys():
        print(f'Account with login {login} is not in data. Check the correctness of the login set')


if __name__ == '__main__':
    log_in_1('picknik', '238rheyf')
    log_in_2('pickn4k', '238rheyf')
