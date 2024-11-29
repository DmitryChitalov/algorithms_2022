from random import randint

def guess_num(number, count=1):
    print(f'Попытка №{count}')
    answer = int(input('Введите целое число от 0 до 100: '))
    if answer == number:
        print('Вы угадали!')
    elif count == 11:
        print(f'Число не отгадано! Правильный ответ {number}')
    else:
        if answer < number:
            print(f'Загаданное число больше')
        elif answer > number:
            print(f'Загаданное число меньше')
        count += 1
        guess_num(number, count)

guess_num(randint(0, 100))