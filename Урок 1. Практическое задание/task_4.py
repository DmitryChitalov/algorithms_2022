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
    "Алексей Иванов": ["1234", "Active"],
    "Барак Обама": ["Patamuchto", "Active"],
    "П": ["3456", "Deleted"]

}

def user_activation(user):
    """
    Делает пользователя активным
    """
    users[user][1] = "Active"
    return True


def user_registration(user, password):
    """
    Регистрация пользователя
    """
    users[user] = [password, "Active"]
    return True

# Ниже Вариант - 1
# Сложность:  T(N) = N^2
def user_check(user):
    """
    Проверка пользователя
    0 - нет пользователя,
    1 - не активен,
    2 - ок
    """
    check_point: int = 0                                   # O(1)
    for name in users.keys():                              # O(N)
        if name == user and users[user][1] != "Active":    # O(len(user)*2)
            check_point = 1                                # O(1)
        elif name == user and users[user][1] == "Active":  # O(len(user)*2)
            check_point = 2                                # O(1)

    return check_point


# Ниже Вариант - 2
# Сложность:  T(N) = 4 * N + 3
# Данный вариант легче
def user_check_2(user):
    """
    Проверка пользователя
    0 - нет пользователя,
    1 - не активен,
    2 - ок
    """
    check_point: int = 0                                   # O(1)
    if user in users and users[user][1] != "Active":       # O(N) + O(N)
        check_point = 1                                    # O(1)
    elif user in users and users[user][1] == "Active":     # O(N) + O(N)
        check_point = 2                                    # O(1)

    return check_point

def body():
    """
    Тело программы
    """
    user = input("Введите пользователя: ")
    if user_check_2(user) == 0:
        print("Полльзователя не существует")
        answer = input("Желаете зарегестрировать пользователя?  (Да/Нет):  ")
        if answer == "Нет":
            return 0
        else:
            password = input("Введите пароль:  ")
            user_registration(user, password)
            return "Registred"
    elif user_check(user) == 1:
        print("Полльзователь не активен")
        answer = input("Желаете активировать пользователя?  (Да/Нет):  ")
        if answer == "Нет":
            return 00
        else:
            user_activation(user)
            return "Пользователь активирован"

    return "Пользователь допущен"

print(body())







