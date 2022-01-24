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

users_dict = {'Thomas': ['Thomas123', True],
              'Elizabeth': ['Elizabeth123', False],
              'Arthur': ['Arthur123', False],
              'Ada': ['Ada1234', True],
              'John': ['John1234', True],
              'Charlie': ['Charlie123', False],
              'Jeremiah': ['Jeremiah123', True],
              'Grace': ['Grace123', False],
              'Winston': ['Winston123', False],
              'Billy': ['Billy123', True]}


def authentication_v1(input_dict, name, password):
    if (name in input_dict.keys()) and (input_dict.get(name)[0] == password):
        if input_dict.get(name)[1]:
            print('Пользователь может быть допущен к ресурсу')
        else:
            print('Необходимо пройти активацию учётной записи')
    else:
        print('Неверная пара логин/пароль')


def authentication_v2(input_dict, name, password):
    for name_dict, pass_auth_dict in input_dict.items():
        if (name_dict == name) and (pass_auth_dict[0] == password):
            if pass_auth_dict[1]:
                result = 'Пользователь может быть допущен к ресурсу'
                break
            else:
                result = 'Необходимо пройти активацию учётной записи'
                break
        else:
            result = 'Неверная пара логин/пароль'
    return print(result)


authentication_v1(users_dict, 'Thomas', 'Thomas123')
authentication_v2(users_dict, 'Grace', 'Grace123')
