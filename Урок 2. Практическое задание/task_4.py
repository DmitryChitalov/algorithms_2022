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


def sum_elem_met(i, chislo, kol_elem, sum_elem):
    if i == kol_elem:
        print(f'Количество эелементов - {kol_elem}, их сумма- {sum_elem}')
    elif i < kol_elem:
        return sum_elem_met(i + 1, chislo / 2 * -1, kol_elem, sum_elem + chislo)


try:
    kol_elem = int(input('Введите количество элементов: '))
    sum_elem_met(0, 1, kol_elem, 0)
except ValueError:
    print('Введена строка, необходимо ввести число')

#  решение через тернарный оператор
# def sum_elem_met(element):
#   return 0 if element == 0 else 1 + sum_elem_met(element - 1) / 2
#
#
# kol_elem = int(input()"Введеите количество элементов: ")
# print(f"Количество эементов: {kol_elem}, их сумма: {sum_elem_met(kol_elem)}")
