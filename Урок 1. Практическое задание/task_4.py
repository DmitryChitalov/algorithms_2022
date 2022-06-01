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

users_base = {
    "user_1": {"is_activated": False,
                "login": "user_1",
                "pass": "24C9E15E52AFC47C225B757E7BEE1F9D"},
    "user_2": {"is_activated": True,
                "login": "user_2",
                "pass:": "7E58D63B60197CEB55A1C487989A3720"},
    "user_3": {"is_activated": True,
                "login": "user_3",
                "pass": "92877AF70A45FD6A2ED7FE81E1236B78"},
    "user_4": {"is_activated": False,
               "login": "user_4",
               "pass": "3F02EBE3D7929B091E3D8CCFDE2F3BC6"}
}

def activate_user(user: dict):
    user['is_activated'] = True                  #O(1)
    print(f"{user.get('Login')} , {user}")       #O(1)


def ask_activate():
    print("Ваша учетная запись не активна!")                                    #O(1)
    answer = input("Активировать вашу учетную запись? (yes or no): \n").lower()  #O(1)
    if answer == 'yes':                                                         #O(1)
        return True                                                             #O(1)
    else:
        return False                                                            #O(1)

# T(n) =  O(1)
def solution_1(user_name):
    result = users_base.get(user_name)      #O(1)
    return result                           #O(1)

# T(n) =  O(n)
def solution_2(user_name):
    for key, value in users_base.items():    # O(n)
        if key == user_name:                 # O(1)
            result = value                   # O(1)
            return result                    # O(1)

def check_status(user_name):
    #info_user = solution__1(user_name) # 1-ый вариант решения
    info_user = solution_2(user_name)  # 2-ый вариант решения
    if info_user and info_user.get("is_activated"):
        print(f"{info_user.get('login')} ваша учетная запись активна")
    elif info_user and not info_user.get("is_activated"):
        if ask_activate():
            activate_user(info_user)
            return print(f"{info_user.get('login')} ваша учетная запись успешно активирована")
        else:
            return print("Аккаунт не активирован")
    else:
        print(f"{user_name}  Пользователь с таким именем отсутствует")
        return False
    return True
print("Available users is system: ", [(x, f'activated: {k.get("is_activated")}') for x, k in users_base.items()])
print(check_status(input("Ваш логин: ")))
