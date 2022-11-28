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
    dict_acc2 = {'login': {}}
    FILENAME = 'accounts.json'
    is_activ = True
    login = input("введите логин: ")
    password = input("введите пароль: ")
    try:
        with open(FILENAME, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            if login in data['login'] and password in data['login'][login] and data['login'][login][
                password] is not is_activ:
                activate_process = input('Необходима активация. Активировать аккаунт?: (д/н)')
                if activate_process.lower() == 'д':
                    dict_acc2['login'].setdefault(login, {}).setdefault(password, [])
                    dict_acc2['login'][login][password] = is_activ
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['login'].setdefault(login, {}).setdefault(password, [])
                            data['login'][login][password] = is_activ
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                else:
                    print('Досвидания!')
    except json.JSONDecodeError:
        print('файл пуст')


def check_ac():
    dict_acc2 = {'login': {}}
    FILENAME = 'accounts.json'
    checkAccount = input("у вас уже есть аккаунт (Д/Н)?")
    if (checkAccount.lower() == 'н'):
        login = input("придумайте логин: ")
        password = input("придумайте пароль: ")
        is_activ = False
        try:
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                if login in data['login']:
                    print("такой логин уже существует, попробуйте снова")
                    check_ac()
                else:
                    dict_acc2['login'].setdefault(login, {}).setdefault(password, [])
                    dict_acc2['login'][login][password] = is_activ
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['login'].setdefault(login, {}).setdefault(password, [])
                            data['login'][login][password] = is_activ
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                            print("Поздравляем, аккаунт создан!")
        except json.JSONDecodeError:
            print('файл пуст')
            dict_acc2['login'].setdefault(login, {}).setdefault(password, [])
            dict_acc2['login'][login][password] = is_activ
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    data['login'].setdefault(login, {}).setdefault(password, [])
                    data['login'][login][password] = is_activ
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                except json.JSONDecodeError:
                    json.dump(dict_acc2, file, ensure_ascii=False, indent=4)
                    print("Поздравляем, аккаунт создан!")

    elif (checkAccount.lower() == 'д'):
        check_is_active()

check_ac()

#Сложность O(n)





















