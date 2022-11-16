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
row_element = 1
i = 0
sum_elements = 1
def sum_numbers(elements):
    global row_element
    global i
    global sum_elements
    if i == elements - 1:
        return
    row_element /= -2
    sum_elements += row_element
    i += 1
    return sum_numbers(elements)

elements = int(input('Введите количество элементов: '))
sum_numbers(elements)
print(f'Количество элементов - {elements}, их сумма - {sum_elements}')
