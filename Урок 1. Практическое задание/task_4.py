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


def authentication_1(login, pas):
    """
    Сложность: O(len(users1))
    :param login: str
    :param pas: str
    """
    if login in users1 and pas == str(users1[login][0]):                                     # O(n)
        for key, val in users1.items():                                                      # O(n)
            if key == login and val[1] == 1:                                                 # O(1)
                print('Добро пожаловать')                                                    # O(1)
                break                                                                        # O(1)
            elif key == login and val[1] == 0:                                               # O(len(users1))
                print('Вам необходимо пройти активацию учетной записи')                      # O(1)
    else:                                                                                    # O(1)
        print('Пользователь с таким логином отсутствует в системе, пройдите регистрацию')    # O(1)


def authentication_2(login, pas):
    """
       Сложность: O(n^2)
       :param login: str
       :param pas: str
    """
    count = 0                                                                 # O(1)
    for i in users2:                                                          # O(n)
        if i == login and str(users2[i]) == pas:                              # O(len(uses2))
            for j in users_auto:                                              # O(n)
                if i == j and users_auto[j] == 1:                             # O(len(uses2))
                    print('Добро пожаловать')                                 # O(1)
                    break                                                     # O(1)
                else:                                                         # O(len(uses2))
                    print('Вам необходимо пройти активацию учетной записи')   # O(1)
                    break                                                     # O(1)
        elif i == login and str(users2[i]) != pas:                            # O(len(uses2))
            print('Введен не верный пароль')                                  # O(1)
            break                                                             # O(1)
        else:                                                                 # O(len(uses2))
            count +=1                                                         # O(1)
            continue                                                          # O(1)
    if count == len(users2):                                                  # O(len(uses2))
        print('Пользователь с таким логином отсутствует в системе, пройдите регистрацию')  # O(1)


if __name__ == '__main__':
    users1 = {'deni': [12345, 1], 'yandex': [12345, 1], 'viki': [54321, 0], 'kiril': [77876, 0]}
    users2 = {'deni': 12345, 'yandex': 12345, 'viki': 54321, 'kiril': 77876}
    users_auto = {'deni': 1, 'yandex': 1, 'viki': 0, 'kiril': 0}
    login = input('Введите Ваш Login: ')
    password = input('Введите Ваш Пароль: ')
    authentication_1(login, password)
    authentication_2(login, password)
    # authentication_2('deni', '12345')
    # authentication_2('den', '12345')
    # authentication_2('viki', '54321')
    # authentication_1('deni', '12345')
    # authentication_1('den', '12345')
    # authentication_1('viki', '54321')
