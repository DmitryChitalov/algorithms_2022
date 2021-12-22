"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!

"""

def fun(h):
    sum_t = 0
    k = h - 1
    if h == 0:
        return sum_t
    return fun(k) + sum_t + ((-1) ** (k % 2) / (1 << k))

try:
    n = int(input("Введите количество элементов: "))
    print(f"Количество элементов: {n}, их сумма: {fun(n)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")

