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
users_list = {
    "user_1": {"is_activated": False,
               "Login": "user_1",
               "password": "hash_pass"},
    "user_2": {"is_activated": True,
               "Login": "user_2",
               "password": "hash_pass"},
    "user_3": {"is_activated": False,
               "Login": "user_3",
               "password": "hash_pass"},
    "user_4": {"is_activated": False,
               "Login": "user_4",
               "password": "hash_pass"},
    "user_5": {"is_activated": False,
               "Login": "user_5",
               "password": "hash_pass"}
}
def is_yes(message: str) -> bool:
    """
    Returns user answer for a question
    :param message: str
    :return: bool
    """
    return input(message).lower() in ("yes", "y", "yea")


def activate_user(user: dict):
    """
    Activate user
    :param user: dict
    """
    user["is_activated"] = True
    print(f"User: {user.get('Login')} is activated, {user}")


def check_user(user_name: str) -> bool:
    """
    Check that user is in system and user account is activated.
    :param user_name: str
    :return: bool
    """
    credentials = user_getter(user_name)                                # solution 1
    credentials = user_getter_2(user_name)                              # solution 2

    if credentials and credentials.get("is_activated"):
        print( f"User {credentials.get('Login')} can use our services")
    elif credentials and not credentials.get("is_activated") and is_yes("your account not activated, activate now?\n"):
        activate_user(credentials)
    else:
        message = "User account not activated" if credentials and not credentials.get("is_activated") \
            else f"User \"{user_name}\" doesn't exist, you can't use our services"
        print(message)
        return False
    return True


""" Solutions: """
def user_getter(name: str) -> dict:
    """
    Algorithm 1:
    Get user by user name and returns user credentials
    :param name: str
    :return: dict or None
    T(n) = 2 => O(1)
    """
    credentials = users_list.get(name)              # O(1)
    return credentials                              # O(1)

def user_getter_2(name: str) -> dict:
    """
    Algorithm 2:
    Get user by user name and returns user credentials.
    :param name: str
    :return: dict
    T(n) = n + 3 => O(n)
    """
    for key, value in users_list.items():           # O(n)
        if key == name:                             # O(1)
            credentials = value                     # O(1)
            return credentials                      # O(1)



print("Available users is system: ", [(x, f'activated: {k.get("is_activated")}') for x, k in users_list.items()])
print(check_user(input("user_name?\n").lower()))



















