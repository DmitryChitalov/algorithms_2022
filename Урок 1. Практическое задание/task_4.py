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

log_pass_dict = {("login1", "pass1"): True, ("login2", "pass2"): False, ("login3", "pass3"): False, ("login4", "pass4"): True}


# O(1) - не зависит от числа элементов log_pass_dict, поэтому это решение эффективнее
def authorization_user(log, pas):
    enter = log_pass_dict.get((log, pas), " ")
    if enter == " ":
        print("Неверный логин/пароль")
    elif not enter:
        answer = input("Активировать учетную запись? да/нет ")
        if answer.lower() == "да":
            log_pass_dict[(log, pas)] = True
            print("Учетная запись активирована")
            print("Вход выполнен")
        else:
            print("Отмена активации")
    else:
        print("Вход выполнен")


# O(n) - если log_pass_dict переменной длины
# O(1) - в нашем случае, т.к. log_pass_dict не меняется
def authorization_user2(log, pas):

    for log_pass in log_pass_dict:
        if (log, pas) == log_pass:
            if not log_pass_dict[(log, pas)]:
                answer = input("Активировать учетную запись? да/нет ")
                if answer.lower() == "да":
                    print("Учетная запись активирована")
                    print("Вход выполнен")
                else:
                    print("Отмена активации")
            else:
                print("Вход выполнен")
            break
    else:
        print("Неверный логин/пароль")


authorization_user("login2", "pass2")
authorization_user("login1", "pass1")
authorization_user("login1", "pass2")

authorization_user2("login2", "pass2")
authorization_user2("login1", "pass1")
authorization_user2("login1", "pass2")



