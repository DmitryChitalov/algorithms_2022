import random

num = int(random.randint(0, 101))
count = 0


def guess_num():
    global count
    count += 1
    user_guess = int(input("Какое число я загадала? "))

    if count == 10:
        return f'Вы проиграли. Загаданное число {num}'
    else:
        if user_guess > num:
            print("Загаданное число меньше")
            return guess_num()
        elif user_guess < num:
            print("Загаданное число больше")
            return guess_num()
        elif user_guess == num:
            return f'Вы угадали число!'


print(guess_num())
