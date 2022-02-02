"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. Решение через цикл не принимается.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230->3210
"""

def recur_method(numb, num_even=0):
    if numb == 0:
        return f'число наоборот: {num_even}'
    else:
        cur_n = numb % 10
        numb = numb // 10
        num_even = num_even * 10
        num_even = num_even + cur_n
        return recur_method(numb, num_even)
try:
    num = int(input("Введите натуральное число: "))
    print(recur_method(num))
except ValueError:
    print('Пожалуйста, вводите только числа')

