""""
Костюкович Николай.1четверть.Алгоритмы и структуры данных.
Урок 2. Рекурсия.
"""
#Задание 1.

def calculator():
    buttons = ('+', '-', '*', '/')
    a = input(f"Введите операцию (+, -, *, / или 0 для выхода): ")
    if a == '0':
        print("Прощаемся!")
        return
    elif a in buttons:
        a1 = input("Введите число: ")
        a2 = input("Введите число: ")
        if a == '+':
            print(f'{a1} {a} {a2} = {float(a1) + float(a2)}')
            calculator()
        elif a == '-':
            print(f'{a1}{a}{a2} = {float(a1) - float(a2)}')
            calculator()
        elif a == '*':
            print(f'{a1}{a}{a2} = {float(a1) * float(a2)}')
            calculator()
        elif a == '/':
            try:
                print(f'{a1}{a}{a2} = {float(a1) / float(a2)}')
            except ZeroDivisionError:
                print("Деление на ноль запрещенно!")
                calculator()
    else:
        print(f'Такого знака операции не существует.Введите знак операции заново!')
        calculator()

calculator()

#Задание 2.
def even_or_add(num, even=0, odd=0):
    if (num % 10) % 2 == 0:
        even += 1

    else:
        odd += 1
    if num > 10:
        even_or_add(num // 10, even,odd)
    else:
        print(f"Четные цифры: ({even})  Нечетные цифры: ({odd})")
        return

even_or_add(int(input("Введите число: ")))

#Задание 3.
def revers_number(number):
    if number == 0:
        return
    else:
        n2 = number[::-1]
        print('"Обратное" ему число:',n2)

revers_number(input("Введите целое число: "))

#Задание 4.
def sequence_sum(n, a=1.0, seq_sum=0, count=0):
    if n == 0:
        print(f'Количество элементов - {count}, их сумма - {seq_sum}')
        return
    else:
        n -= 1
        count += 1
        seq_sum += a
        sequence_sum(n, a/(-2), seq_sum, count)
try:
    print(int(input("Введите колл элем: ")))
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")


sequence_sum(int(input(f'Введите количество элементов: ')))

#Задание 5.

def symbol_table(num=32, count=1):
    if num >= 128:
        return
    else:
        if count < 10:
            print(f'{num} - {chr(num)} ', end="")
        else:
            print(f'{num} - {chr(num)}')
            count = 0
        symbol_table(num + 1, count + 1)


symbol_table()

#Задание 6.

import random

def guessesTaken(a, count=1):

    user_guess = int(input("Угадайте число от 1 до 100: "))
    if count > 9:
        print(f"Вы угадали!!! Загаданное число {a}")
        return
    if user_guess == a:
        print(f"Вы отгодали число {a} за {count} попыток")
        return

    elif user_guess > a:
        print("Ваше число слишком большое!")
        guessesTaken(a, count+1)
    else:
        print("Ваше число слишком маленькое!")
        guessesTaken(a, count +1)

guessesTaken(random.randint(1,100))

#Задание 7.













