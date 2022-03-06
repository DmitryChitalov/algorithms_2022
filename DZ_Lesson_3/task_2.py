import hashlib, json

print("программа может хранить только одного пользователя и один пароль к нему")

begin_input = input("1. регистрация\n2. вход\n: ")
if begin_input == "1":
    login_user_1 = input("login: ")  # логин первого пользователя, я использую как соль для хэша
    user_1 = input("passwrd: ")  # первый запрос пароля
    DB_json_1 = {login_user_1: hashlib.sha256(user_1.encode()).hexdigest()}

    print(hashlib.sha256(user_1.encode() + login_user_1.encode()).hexdigest())
    json.dump(DB_json_1, open("hash.txt", "w"))
    print("вы зарегестрированы")

if begin_input == "2":
    login_user_2 = input("login: ")  # логин второго пользователя, я использую как соль для хэша
    user_2 = input("passwrd: ")  # второй запрос пароля

    print(hashlib.sha256(user_2.encode() + login_user_2.encode()).hexdigest())

    try:
        if hashlib.sha256(user_2.encode()).hexdigest() == json.load(open("hash.txt"))[login_user_2]:
            print("пароли совпадают, вы в системе :)")
        else:
            print("ошибка, вас нет в системе")
    except:
        print("еще никто не регестрировался в системе")





