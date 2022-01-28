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


def row_generic(f, n) -> float:
    if n == 0:
        return 0
    else:
        return f + row_generic(f/-2, n - 1)


if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    print(f"Количество элементов - {n}, Сумма элементов ряда:", row_generic(1, n))
