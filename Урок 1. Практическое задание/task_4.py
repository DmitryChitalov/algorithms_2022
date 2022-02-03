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


from functools import reduce
import operator


def user_verification_during_authorization_first_way(users_of_web_resource, user_name, user_password):  # O(n)
    for index in range(len(users_of_web_resource)):  # O(n)
        if users_of_web_resource[index][0] == user_name and users_of_web_resource[index][1] == user_password \
                and users_of_web_resource[index][2]:  # O(1)
            return "Добро пожаловать! Доступ к ресурсу предоставлен!"  # O(1)
        elif users_of_web_resource[index][0] == user_name and users_of_web_resource[index][1] == user_password \
                and not users_of_web_resource[index][2]:  # O(1)
            return "Учётная запись неактивна! Пройдите активацию!"  # O(1)
        elif users_of_web_resource[index][0] == user_name and users_of_web_resource[index][1] != user_password:
            return "Пароль неверный"  # O(1)
    return "Данного пользователя не существует"  # O(1)


def user_verification_during_authorization_second_way(users_of_web_resource, user_name, user_password):  # O(n**2)
    if user_name in reduce(operator.concat, users_of_web_resource)\
            and reduce(operator.concat,  # O(n**2)
                       users_of_web_resource)[reduce(operator.concat,
                                                     users_of_web_resource).index(user_name) + 1] == user_password \
            and reduce(operator.concat,
                       users_of_web_resource)[reduce(operator.concat,
                                                     users_of_web_resource).index(user_name) + 2]:
        return "Добро пожаловать! Доступ к ресурсу предоставлен!"
    elif user_name in reduce(operator.concat, users_of_web_resource)\
            and reduce(operator.concat,
                       users_of_web_resource)[reduce(operator.concat,
                                                     users_of_web_resource).index(user_name) + 1] == user_password \
            and not reduce(operator.concat,
                           users_of_web_resource)[reduce(operator.concat, users_of_web_resource).index(user_name) + 2]:
        return "Учётная запись неактивна! Пройдите активацию!"
    elif user_name in reduce(operator.concat, users_of_web_resource)\
            and reduce(operator.concat,
                       users_of_web_resource)[reduce(operator.concat,
                                                     users_of_web_resource).index(user_name) + 1] != user_password:
        return "Пароль неверный"
    return "Данного пользователя не существует"  # O(1)


"""
Первая реализация будет намного эффективнее,
так как в ней не используются методы из импортируемых модулей,
которые имеют квалратичнцю сложность.
"""


list_of_users_of_web_resource = [['n1', 'p1', True], ['n2', 'p2', True], ['n3', 'p3', False],
                                 ['n4', 'p4', True], ['n5', 'p5', False]]


print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n1', 'p1'))
print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n1', '21p1'))
print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n3', 'p3'))
print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n5', 'p5'))
print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n4', 'p4'))
print(user_verification_during_authorization_first_way(list_of_users_of_web_resource, 'n3453', 'p4'))


print(user_verification_during_authorization_second_way(list_of_users_of_web_resource, 'n1', 'p1'))
print(user_verification_during_authorization_second_way(list_of_users_of_web_resource, 'n5671', 'p1'))
print(user_verification_during_authorization_second_way(list_of_users_of_web_resource, 'n5', 'p5'))
print(user_verification_during_authorization_second_way(list_of_users_of_web_resource, 'n4', 'p5345'))

