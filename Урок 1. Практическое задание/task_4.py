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
dictionary_2 = {"Kolya": ["1234", "activate"],
                "Natalya": ["5678", "not_activate"]}


# первое решение


def check_person(dict_example):  # O(n^2)
    a = input("enter login ")  # O(1)
    b = input("enter password ")  # O(1)
    i = 0  # O(1)
    while i < len(dict_example):  # O(n)
        for key, value in dict_example.items():  # O(n)
            if key == a:  # O(1)
                if value[1] == "activate" and value[0] == b:  # O(1)
                    return print("Verified")  # O(1)
                elif value[1] == "not_activate" and value[0] == b:  # O(1)
                    return print("Activate your account")  # O(1)
            elif key != a or value[0] != b:  # O(1)
                i += 1  # O(1)
        return print("Login or password not correct. Pls try again")  # O(1)


# второе решение


def check_person_2(dict_example):  # O(1)
    a = input("enter login")  # O(1)
    b = input("enter password")  # O(1)
    if dict_example.get(a):  # O(1)
        if dict_example[a][0] == b and dict_example[a][1] == "activate":  # O(1)
            return print("Verified")  # O(1)
        elif dict_example[a][0] == b and dict_example[a][1] == "not_activate":  # O(1)
            return print("Activate your account")  # O(1)
        elif dict_example[a][0] != b:  # O(1)
            return print("Password not correct")  # O(1)
    else:
        return print("Login not correct")


print(check_person_2(dictionary_2))
