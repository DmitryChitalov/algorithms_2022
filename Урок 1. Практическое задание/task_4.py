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


class User:
    def __init__(self, name, password, activated):
        self.name = name
        self.password = password
        self.activated = activated


class Result:
    access_granted = "Доступ рашрешен"
    account_not_activated = "Учетная запись не активирована"
    invalid_login_or_password = "Неверный логин или пароль"


list_users = [User("Ivan", "12345", True), User("Galina", "mel223", True), User("Maksim", "bro777", False)]
dict_users = {"Ivan": User("Ivan", "12345", True), "Galina": User("Galina", "mel223", True),
               "Maksim": User("Maksim", "bro777", False)}


# Сложность O(N), необходимо перебрать весь список
def new_user_list(login, password):
    for user in listOfUsers:
        if user.name == login and user.password == password:
            if user.activated:
                return Result.access_granted
            else:
                return Result.account_not_activated
    return Result.invalid_login_or_password


# Сложность O(1), доступ в словарь по ключу
def new_user_dict(login, password):
    user = dictOfUsers.get(login)
    if user != None:
        if user.name == login and user.password == password:
            if user.activated:
                return Result.access_granted
            else:
                return Result.account_not_activated
    return Result.invalid_login_or_password

# Вывод - в данном случае словарь - сложность O(1)  предпочтительней списка так как константная, выполняется быстрее и за постояннное время.
