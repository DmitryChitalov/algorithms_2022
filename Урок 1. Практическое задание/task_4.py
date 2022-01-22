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

users = {
    "Andrey": {"Password": "123456",
               "Activate": True},
    "Kiril": {"Password": "654321",
              "Activate": False},
    "Yuri": {"Password": "135246",
             "Activate": True},
    "Alex": {"Password": "246135",
             "Activate": False},
    "Mikhail": {"Password": "531642",
                "Activate": True}
}


def log_in_v1(username):
    pass


def log_in_v2(username):
    pass
