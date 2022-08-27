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

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def reverse_number(num, reverse_num=''):
    if num == 0:  # Базовый случай
        return reverse_num
    elif num < 0:
        reverse_num += '-'
        num = abs(num)

    next_digit = num % 10
    reverse_num += str(next_digit)
    return reverse_number(num // 10, reverse_num)


if __name__ == '__main__':
    number = int(input('Введите число, которое требуется перевернуть: '))
    print('Перевернутое число:', reverse_number(number))
