
spisok = {"user_1": [707707, True],
          "user_2": [808808, False],
          "user_3": [909909, True],
          "user_4": [708809, False]}

def alg_one(llist): # O(N)
    for i in llist: # O(N)
        if llist[i][1] == True: # O(N)
            print("activated!") # O(1)
        else:
            print("no activated! -", i) # O(1)


def alg_two(users, user_name, user_password): # O(1)
    if users.get(user_name):
        if users[user_name][0] == user_password and users[user_name][1]:
            return "Пароль верный!"

        elif users[user_name][0] == user_password and not users[user_name][1]:
            return "Пройдите активацию!"

        elif users[user_name][0] != user_password:
            return "Пароль не верный!"
    else:
        return "Данного пользователя нет!"

alg_one(spisok)
print(alg_two(spisok, "user_2", 808808))

'''
более лучший алгоритм - первый
егосложность константна(лучше чем линейная сложность)
'''