
#Задание 4.

#Сложность O(n**3)
web_users=[{'login': 'hi', 'password': 'hello34', 'activated': 'yes'}, {'login': 'boris', 'password': 'boriska345', 'activated': 'no'},
           {'login': 'nastya','password': 'nastusha82', 'activated':'yes'}, {'login': 'anna', 'password': 'anna98', 'activated': 'no'}]
#O(1)

def find_user():
    user = str((input("Введите свой логин: "))) #O(1)
    for i in web_users: #O(n)
            if user in i['login']: #O(n)
                if i['activated'] == 'no': #O(n)
                    print(f"Пользователь с логином {user} не активирован. Вам нужно пройти активацию") #O(1)
                elif i['activated'] == 'yes': #O(n)
                    print(f"Вы активированы") #O(1)

find_user()
#T(n)=1+n*n*n+1+n+1+1=4+2n**3

#Сложность O(n)
web_users2=[{'login': 'hi', 'password': 'hello34', 'activated': 'yes'}, {'login': 'boris', 'password': 'boriska345', 'activated': 'no'},
           {'login': 'nastya','password': 'nastusha82', 'activated':'yes'}, {'login': 'anna', 'password': 'anna98', 'activated': 'no'}]
#O(1)
not_activated={i['login'] for i in web_users2 if i['activated']=='no' } #O(n)
activated = {i['login'] for i in web_users2 if i['activated']=='yes' } #O(n)
def find_user2():
    user = str((input("Введите свой логин: "))) #O(1)
    if user in not_activated: #O(n)
        print(f'Пользователь с логином {user} не активирован. Вам нужно пройти активацию') #O(1)
    else:
        print(f"Вы активированы") #O(1)

find_user2()
#T(n)=1+n+n+1+n+1+1=4+3n