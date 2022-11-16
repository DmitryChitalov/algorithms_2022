"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_one(count, summand=1, counter=1, sum=0):
    if counter == count:
        return sum + summand
    elif count == 0:
        return 0
    elif summand > 0:
        return sum_one(count, -(summand / 2), counter + 1, sum + summand)
    elif summand < 0:
        return sum_one(count, abs(summand / 2), counter + 1, sum + summand)


user_input = int(input('Введите количество элементов: '))

print(f'Количество элементов: {user_input}\nИх сумма: {sum_one(user_input)}')
