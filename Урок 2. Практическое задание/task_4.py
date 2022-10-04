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


def sequence05(step_left, current_sum=0, current_value=1):
    global step
    # print(f' step_left = {step_left} , current_sum = {current_sum}, current_value = {current_value} ')
    if step_left == 0:
        print(f' number of elements = {step}, their summa = {current_sum}  ')
        return
    else:
        current_sum += current_value
        current_value = current_value / -2
        step_left -= 1
        sequence05(step_left, current_sum, current_value)


def digit_input():
    while True:
        try:
            num = int(input("\n Please enter an INT  number >= 1:   "))
            if num < 1:
                continue
            return num
        except ValueError:
            continue


if __name__ == '__main__':
    step = digit_input()
    sequence05(step)

# Script listing:
#
#  Please enter an INT  number >= 1:   3
#  number of elements = 3, their summa = 0.75
#
# Process finished with exit code 0