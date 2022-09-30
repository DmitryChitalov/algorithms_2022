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

user_dict = {
    "Fox": {"password": 123, "is_active": True},
    "Bin": {"password": 456, "is_active": False},
    "Kim": {"password": 789, "is_active": False}

}
print(user_dict["Fox"])


# Способ 1
# Сложность: O(1) — константное время
def check_is_active():
    user_input = input("Введите логин: ")  # O(1)
    try:
        if user_dict[user_input]["is_active"] is False:  # O(1)
            print("Для доступа к ресурсу необходимо активировать учетную запись.")  # O(1)
        else:
            print("Доступ разрешен")  # O(1)
    except KeyError:
        print("Ошибка! Введен неверный логин.")  # O(1)


check_is_active()


# Способ 2
# Сложность: O(n) линейное время
def check_is_active_2():
    user_input = input("Введите логин: ")  # O(1)
    try:
        for i in user_dict[user_input]:  # O(n)
            if user_dict[user_input]["is_active"] is False:  # O(1)
                print("Для доступа к ресурсу необходимо активировать учетную запись.")  # O(1)
            else:
                print("Доступ разрешен")  # O(1)
            break
    except KeyError:
        print("Ошибка! Введен неверный логин.")  # O(1)


check_is_active_2()

'''
Первый способ решения эффективнее, 
т.к. при константной сложности выполнения функция работает быстрее, 
чем при линейной.
'''
