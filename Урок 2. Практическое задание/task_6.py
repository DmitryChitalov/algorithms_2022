"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""


from random import randint

def guess_number(wish_digit, tries = 10):
    if tries == 0:
        print(f" You haven't tries more , sorry you loose ")
        return
    print(f' You have {tries} tries more')
    try_digit = digit_input()
    if try_digit == wish_digit:
        print(f' You Win! Congrats! ')
        return
    if try_digit < wish_digit:
        print(f' Try  bigger digit')
        tries -= 1
        guess_number(wish_digit, tries)
    if try_digit > wish_digit:
        print(f' Try  smaller digit')
        tries -= 1
        guess_number(wish_digit, tries)


def digit_input():
    while True:
        try:
            num = int(input(" please enter digit 1...100  :  "))
            return num
        except ValueError:
            continue


if __name__ == '__main__':
    print(f'\n -- Generation Random Number --- ')
    num = randint(1, 100)
    print(f' -- Try to guess the wish number -- \n')
    # print(f' wish number = {num}')
    guess_number(num)

# script listing
#
#  -- Generation Random Number ---
#  -- Try to guess the wish number --
#
#  You have 10 tries more
#  please enter digit 1...100  :  50
#  Try  smaller digit
#  You have 9 tries more
#  please enter digit 1...100  :  25
#  Try  bigger digit
#  You have 8 tries more
#  please enter digit 1...100  :  37
#  Try  bigger digit
#  You have 7 tries more
#  please enter digit 1...100  :  43
#  Try  smaller digit
#  You have 6 tries more
#  please enter digit 1...100  :  40
#  Try  bigger digit
#  You have 5 tries more
#  please enter digit 1...100  :  41
#  You Win! Congrats!
#
# Process finished with exit code 0