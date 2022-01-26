import hashlib

def enter():
    f = open("log&pass.csv", "r+", encoding="utf-8")
    login = input('Login: ')
    password = input('Password: ')
    for i in f:
        if i[:i.index(';')] == login:
            if i[i.index(';') + 1:].replace("\n", '') == hashlib.sha256(login.encode() + password.encode()).hexdigest():
                print(f"password_hash: {hashlib.sha256(login.encode() + password.encode()).hexdigest()}")
                return print("Welcome back!")
            else:
                print('Password is wrong')
                return enter()
    ans = input(f'There is no such login as {login}, wanna register?\n')
    f.close()
    if ans.lower() == 'yes':
        f = open("log&pass.csv", "r+", encoding="utf-8")
        login = input('Enter your new login: ')
        for i in f:
            if i[:i.index(';')] == login:
                print('login already exists')
                return enter()
        password = input('Enter your new password: ')
        f.readlines()
        f.writelines(f'{login};{hashlib.sha256(login.encode() + password.encode()).hexdigest()}\n')
        f.close()
        print(f"new_password_hash: {hashlib.sha256(login.encode() + password.encode()).hexdigest()}")
        enter()
    else:
        return print('Goodbye')
enter()