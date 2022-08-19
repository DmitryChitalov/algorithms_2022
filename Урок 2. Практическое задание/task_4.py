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


def sum_of_elements(count, first_elem=-2):
    if count == 0:
        return 0
    first_elem = -(first_elem / 2)
    count -= 1
    return first_elem + sum_of_elements(count, first_elem)


def sum_of_elements_user_interface():
    count = int(input('Введите количество элементов: '))
    return f'Количество элементов - {count}, их сумма - {sum_of_elements(count)}'


if __name__ == '__main__':
    print(sum_of_elements_user_interface())
