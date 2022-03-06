import random
random_num = random.randint(0, 100)
def otg_chislo(count = 0):
    if count == 10:
        print("попытки кончиличь!")
        return random_num
    user = int(input(": "))

    if user == random_num:
        print("вы отгадали")
    else:
        if user < random_num:
            print("Ваше число меньше чем загаданое")
            return otg_chislo(count+1)
        else:
            print("Ваше число больше чем загаданое")
            return otg_chislo(count+1)

otg_chislo()