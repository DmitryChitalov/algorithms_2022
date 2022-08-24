"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def game(nubmer=random.randint(1, 100)):
    print(nubmer)
    count = 0
    max_count = int(input("введите количество попыток :"))
    if max_count > 0:
        count += 1
        max_count -= 1
        user_number = int(input(f"попытка № {count}, осталось {max_count} введите число: "))

        if user_number == nubmer:
            print("Победа")

        else:
            print("вы проиграли ")
            return game()


game()

# import random
#
# number = None
# userNumber = None
# count = 0
# level = int(input("введите количество попыток :"))
# maxCount = level
#
#
# print(f"Всего попыток {maxCount}")
#
# number = random.randint(1, 100)
#
# while True:
#     count += 1
#     maxCount -= 1
#     print(number)
#     userNumber = int(input(f"попытка № {count}, осталось {maxCount} введите число: "))
#
#     if number == userNumber:
#         print("Победа")
#         user = int(input("Еще разок ? если да то 1 если нет то 2: "))
#         if user == 1:
#             count = 0
#             maxCount = level
#             number = random.randint(1, 100)
#             continue
#         else:
#             break
#
#     if maxCount < 1:
#         print("вы проиграли ")
#         user = int(input("Еще разок ? если да то 1 если нет то 2: "))
#         if user == 1:
#             count = 0
#             maxCount = level
#             number = random.randint(1, 100)
#             continue
#         else:
#             break
#
#     elif number < userNumber:
#         print("введите число меньше")
#
#     elif number > userNumber:
#         print("введите число больше")