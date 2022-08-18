"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
#6
import random

def ugadaika(n,count=10):
    if count != 0:
        print(f'Угадайте число. Количество попыток равно - {count}')
        user_num = int(input("Введите число - "))
        if user_num == n:
            return f'Срочно за лотереей'
        elif user_num > n:
            count-= 1
            print("Много")
            return ugadaika(n,count)
        else:
            count-=1
            print("Мало")
            return ugadaika(n,count)
    else:
        return f"число было {n} - повезет в другой раз"

random_number = random.randint(0, 100)
print(ugadaika(random_number))
