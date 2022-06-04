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


#Рекурсия: нужно выделить несколько изменяемых из итерации рекурсии в последующую итерацию объектов,
# которые будут передатваться в качестве исходных значений в рекурсивную функцию. Условие выхода из
# рекурсии должно быть завязано на значение одного из этих объектов.


def sum_elements_of_series_of_numbers(value_of_current_element, current_number_of_remaining_elements,
                                      current_sum_of_elements):
    if current_number_of_remaining_elements > 0:
        current_sum_of_elements += value_of_current_element
        return sum_elements_of_series_of_numbers(
            -0.5 * value_of_current_element, current_number_of_remaining_elements - 1, current_sum_of_elements)
    elif current_number_of_remaining_elements == 0:
        return current_sum_of_elements
    else:
        pass


number_of_elements = int(input("Введите количество элементов: "))


print(sum_elements_of_series_of_numbers(1, number_of_elements, 0))

