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

activated = True
not_activated = False
users = {"pangxie123123": ["dsjkfs345", activated],
         "y_titova": ["jhhjg1919", activated],
         "ziyouderen": ["jsdha34jsfd", not_activated],
         "tvoy_zaychik": ["hsdfjs12", activated],
         "Dragonfly": ["asfgd769", activated]
         }


# O(n)
def check_activation(lst):
    for k, v in lst.items():  # O(n)
        if v[1] == activated:  # O(1)
            print("Access granted.")  # O(1)
        else:
            print(f"Access denied. Dear {k}, please, activate your account.")  # O(1)


check_activation(users)