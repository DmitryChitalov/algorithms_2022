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
import json

def check_is_active():
    dict_acc2 = {'user1': {'password': '11111', 'activation': True},
                'user2': {'password': '11111', 'activation': False},
                 'user3': {'password': '11111', 'activation': True},
                'user4': {'password': '11111', 'activation': False}
                 }
    FILENAME = 'accounts.json'
    is_activ = True
    login = input("введите логин: ")
    password = input("введите пароль: ")
    try:
        with open(FILENAME, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            if data.get(login):
                if data[login]['password'] == password and data[login]['activation']:
                    print("Добро пожаловать! Доступ к ресурсу предоставлен")
                elif data[login]['password'] == password and not data[login]['activation']:
                    activate_process = input('Необходима активация. Активировать аккаунт?: (д/н)')
                    if activate_process.lower() == 'д':
                        dict_acc2[login] = {'password': password, 'activation': is_activ}
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data[login] = {'password': password, 'activation': is_activ}
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                                print('аккаунт активирован!')
                    else:
                        print('Досвидания!')
    except json.JSONDecodeError:
        check_ac()


def check_ac():
    dict_acc2 = {'user1': {'password': '11111', 'activation': True},
                'user2': {'password': '11111', 'activation': False},
                'user3': {'password': '11111', 'activation': True},
                'user4': {'password': '11111', 'activation': False}
                }
    FILENAME = 'accounts.json'
    checkAccount = input("у вас уже есть аккаунт (Д/Н)?")
    if (checkAccount.lower() == 'н'):
        login = input("придумайте логин: ")
        password = input("придумайте пароль: ")
        is_activ = False
        try:
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                if data.get(login):
                    print("такой логин уже существует, попробуйте снова")
                    check_ac()
                else:
                    dict_acc2[login] = {'password': password, 'activation': is_activ}
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data[login] = {'password': password, 'activation': is_activ}
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                            print("Поздравляем, аккаунт создан!")
        except json.JSONDecodeError:
            dict_acc2[login] = {'password': password, 'activation': is_activ}
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    data[login] = {'password': password, 'activation': is_activ}
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                except json.JSONDecodeError:
                    json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                    print("Поздравляем, аккаунт создан!")

    elif (checkAccount.lower() == 'д'):
        check_is_active()

check_ac()
#Сложность O(n)

# Общая сложность O(n)
def authorization_f(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать! Доступ к ресурсу предоставлен"
            elif value['password'] == user_password \
                    and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif value['password'] != user_password:
                return "Пароль не верный"

    return "Данного пользователя не существует"


# общая сложность O(1)
def authorization_s(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:
            return "Добро пожаловать! Доступ к ресурсу предоставлен"
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:
            return "Учетная запись не активна! Пройдите активацию!"
        elif users[user_name]['password'] != user_password:
            return "Пароль не верный"
    else:
        return "Данного пользователя не существует"

"""Третья реализация в сравнении со второй будет намного эффективнее,
#так как в ней не используется цикл,
#поиск в словаре по ключу имеет сложность - O(1)"""





















