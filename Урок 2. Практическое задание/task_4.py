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

def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)


def sum_array(amount_elements, current_element = 1):
    if amount_elements == 1:
        return current_element
    return current_element + sum_array(amount_elements - 1, current_element / -2)

    

amount_elements = get_number('Enter amount of elements for range (1 -0.5 0.25 ...): ')

print(f'Sum elements: {sum_array(amount_elements)}')