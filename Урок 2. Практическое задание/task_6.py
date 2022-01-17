"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)

def quessing_game(hidden_number, remaining_try = 10):
    quess = get_number(f'Try quess number, you have left {remaining_try} attempts: ')

    if quess == hidden_number:
        print('You win')
        return

    remaining_try -= 1

    if not remaining_try:
        print(f'You lose, {hidden_number=}')
        return

    prompt_proximity = ''

    if abs(quess - hidden_number) < 10:
        prompt_proximity = 'but very hot!'

    if quess > hidden_number:
        prompt_big_or_low = "big"   
    elif quess < hidden_number:
        prompt_big_or_low = "low"
    
    if prompt_big_or_low and prompt_proximity:
        prompt_common = f'You enter too {prompt_big_or_low} number, {prompt_proximity}'
    elif prompt_big_or_low and not prompt_proximity:
        prompt_common = f'You enter too {prompt_big_or_low} number!'
    
    if prompt_big_or_low:
        print(prompt_common)

        

    quessing_game(hidden_number, remaining_try)


hidden_number = random.randint(0, 100)

quessing_game(hidden_number)