import random


def recur_method(count, numb):
    """Рекурсия"""
    print(f"Попытка №{count}")
    answer = int(input("Введите число от 0 до 100: "))
    if count == 10 or answer == numb:
        if answer == numb:
            print("Верно!")
        print(f"Загаданное число: {numb}")
    else:
        if answer > numb:
            print(f"Загаданное число меньше чем {numb}")
        else:
            print(f"Загаданное число больше чем {numb}")
        recur_method(count + 1, numb)


recur_method(1, random.randint(0, 100))
