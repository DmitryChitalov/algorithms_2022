"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

secret_number = randint(0, 100)

def game_secret(counter: int = 0):
    if counter < 10:
        try:
            issues = int(input('Угадайте число : '))
            if issues < secret_number:
                print('Число больше ! ')
                return game_secret(counter =counter + 1)
            elif issues > secret_number:
                print('Число меньше !')
                return game_secret(counter =counter + 1)
            elif issues == secret_number:
                return f'Ура Победа!   Число - {secret_number}'
        except ValueError:
                print('Неправильный ввод. Введите число!')
                game_secret()
    else:
        return f'В следующий раз повезет! Поражение! Число - {secret_number}'

print(game_secret())