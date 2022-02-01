import random


def recur_method(count, num):

    print(f'Попытка № {count}')
    answer = int(input("Введите число от 0 до 100: "))
    if count == 10 or answer == num:
        if answer == num:
            print("Верно")
        print(f'Загаданное число: {num}')
    else:
        if answer > num:
            print(f'Загаданное число меньше, чем: {answer}')
        else:
            print(f'Загаданное число больше, чем: {answer}')
        recur_method(count + 1, num)


recur_method(1, random.randint(0, 100))
