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


def weird_sum(n, previous_sum=float(1), count=1):    
    if count == n:
        return print(f"Количество элементов - {n}, их сумма - {previous_sum}")
    count += 1    
    previous_sum = previous_sum / (-2)
    return weird_sum(n, previous_sum, count)


numbers_quantity = int(input("Введите количество элементов: "))
weird_sum(numbers_quantity)




