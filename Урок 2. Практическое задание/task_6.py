"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randrange


def guess_number(key,attempt=10):
    if attempt == 0:
        return print(f"Закончились попытки. Число - {key}")
    elif attempt == 10:
        print("Загадали число от 0 до 100. Попробуйте угадать")

    option = int(input("Ваш вариант:"))
    if (option == key):
        return print(f" Вы угадали! число {key}")
    elif option > key:
        attempt = attempt - 1
        print(f"Число меньше. Осталось {attempt} попыток")
        guess_number(key,attempt)
    elif option < key:
        attempt = attempt - 1
        print(f"Число больше. Осталось {attempt} попыток")
        guess_number(key, attempt)



guess_number(randrange(0,100))