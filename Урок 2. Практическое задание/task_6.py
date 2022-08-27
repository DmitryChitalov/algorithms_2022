# """
# Задание 6.	В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
#
# Решите через рекурсию. В задании нельзя применять циклы.
# """
#
from random import randint
num = randint(0, 100)
def rec(count=1):
    try:
        attempt = int(input("Введите число от 0 до 100 включительно"))
        if count < 10:
            if attempt != num:
                if attempt > num:
                    print("Загаданное число меньше вашего предположения! Попробуйте еще!")
                elif attempt < num:
                    print("Загаданное число больше вашего предположения! Попробуйте еще!")
                return rec(count=count + 1)
            else:
                print("Ура! Вы угадали!")
        else:
            print(f'Попытки исчерпаны, вы проиграли. Загаданное число: {num}')
    except ValueError:
        print('Вы вместо числа ввели строку ((( Исправьтесь!')
        return rec(count=count + 1)
rec()







