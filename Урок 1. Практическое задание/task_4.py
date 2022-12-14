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
users = {'donttouchme@gmail.com': {"password": '123456789a',
                                   "activated": False},
         'frankghalager@gmail.com': {"password": 'booze4life',
                                     "activated": True},
         'luizaservantes@gmail.com': {"password": 'testpasssword123',
                                      "activated": False}}


def authorisation_1(login: str, password: str):
    """
    Функия проверяет есть ли такой пользователь в хранилище
    после проверяет совпадает ли пароль если пароль совпла проверяет активирована ли учетка если нет отсылает сообщение
    с просьбой пройти верификацию простые If elif else
    :param login: логин
    :param password: пароль
    :return: True или False
    сложность : O(n ^ 2) линейное
    """
    # проверка на существование пользователя
    if login in users.keys():  # O(n)
        # проверка на совпдение пароля
        if password in users[login].values():  # O(n)
            #  проверка на октивацию
            if users[login]['activated']:  # O(1)
                print("Complete")  # O(1)

                return True  # O(1)

            else:
                print("You need to activate your account please follow the instructions below..")  # O(1)
                return False  # O(1)

        else:
            print("Password is wrong")  # O(1)

            return False  # O(1)

    else:
        print("No user registered with this login")  # O(1)

        return False  # O(1)


def authorisation_2(login: str, password: str):
    """
    Функия проверяет есть ли такой пользователь в хранилище
    после проверяет совпадает ли пароль если пароль совпла проверяет активирована ли учетка если нет отсылает сообщение
    с просьбой пройти верификацию
    ФУнкция берет по одному поьзователю в итерации и проверяет равно ли оно входному значению
    если да первой переменной user_exists присваевается Значение True
    ДАльше берет пороль уже по ключу и сравнивает его со входными данными если совпало присваивается значение True
    еременной password_Correct
    третей переменной присваевается значение которое хранится в словаре под ключем activated
    :param login: логин
    :param password: пароль
    :return: True или False
    Сложность алгоритма O(n) :  линейное
    """
    user_exists = False  # O(1)

    # проверка на существование записи
    for user in users.keys():  # O(n)
        if user == login:  # O(1)
            user_exists = True  # O(1)
            break  # O(1)

    if user_exists:  # O(1)
        password_correct = users[login]['password'] == password  # O(1)
        activated = users[login]['activated']  # O(1)
        if password_correct:  # O(1)
            if activated:  # O(1)
                print("Access granted")  # O(1)
                return True # O(1)
            else:
                print("You need to activate your account please follow the instructions below..")  # O(1)
                return False # O(1)
        else:
            print("Password is incorrect")  # O(1)
            return False  # O(1)
    else:
        print("User doesn't  exists")  # O(1)
        return False  # O(1)

# тесты первой функции
if __name__ == '__main__':
    print(authorisation_1.__name__)
    print(authorisation_1("donttouchme@gmail.com", '123456789a'))
    print(authorisation_1("frankghalager@gmail.com", 'booze4life'))
    print(authorisation_1("luizaservantes@gmail.com", 't1estpasssword123'))
    print(authorisation_1("wrong@gmail.com", 't1estpasssword123'))
    # тесты второй функции
    print(authorisation_2.__name__)
    print(authorisation_2("donttouchme@gmail.com", '123456789a'))
    print(authorisation_2("frankghalager@gmail.com", 'booze4life'))
    print(authorisation_2("luizaservantes@gmail.com", 't1estpasssword123'))
    print(authorisation_2("wrong@gmail.com", 't1estpasssword123'))