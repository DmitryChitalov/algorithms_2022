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
num = int(input("Введите  целое число"))

def rec(num_1=1, num_2=0, count=0, res=1):
    if count < num - 1:
        num_2 = num_1 * (-0.5)
        res = res + num_2
        return rec(num_1=num_2, num_2=0, count=count + 1, res=res)
    else:
        print(res)
        return res
rec()





count = int(input("Введите целое число"))


def recursive(idx: int, value: float) -> float:
    current_value = idx * -0.5
    if value:
        return value + recursive(idx=idx + 1, value=current_value)
    else:
        return current_value
