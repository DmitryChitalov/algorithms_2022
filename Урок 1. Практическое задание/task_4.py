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
users = [
    {"Login": "1", "Password": "111111", "is_active": True},
    {"Login": "2", "Password": "222222", "is_active": False},
    {"Login": "3", "Password": "333333", "is_active": False},
    {"Login": "4", "Password": "444444", "is_active": True},
    {"Login": "5", "Password": "555555", "is_active": True}
]


# 1 O(n)
def authentication(login, password):
    for i in users:
        if i.get("Login") == login:
            if i.get("Password") == password:
                if i.get("is_active"):
                    return f'Access allowed'
                else:
                    return f'Please activate your account'
            else:
                return f'Wrong password'


print(authentication("1", "222222"))
print(authentication("2", "222222"))
print(authentication("1", "111111"))

# 2 O(1)
users2 = {"1": {"Password": "111111", "is_active": True},
          "2": {"Password": "222222", "is_active": False},
          "3": {"Password": "333333", "is_active": False},
          "4": {"Password": "444444", "is_active": True},
          "5": {"Password": "555555", "is_active": True}}


def authentication2(user_list, login, password):
    if user_list.get(login):
        if user_list[login]["Password"] == password and user_list[login]["is_active"]:
            return f'Access allowed'
        elif user_list[login]["Password"] == password and not user_list[login]["is_active"]:
            return f'Please activate your account'
        elif user_list[login]["Password"] != password:
            return f'Wrong password'
    else:
        return f'Please create account'


print(authentication2(users2, "1", "222222"))
print(authentication2(users2, "2", "222222"))
print(authentication2(users2, "1", "111111"))
