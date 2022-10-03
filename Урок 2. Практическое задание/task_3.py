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
1230->0321
"""


def reverse_number(inp_num, reverse_str=''):
    # print(f'inp_num = {inp_num} ,reverse_str = {reverse_str} ')
    num1 = inp_num % 10
    reverse_str += str(num1)
    if inp_num < 10:
        print(f'\n reverse_num = {reverse_str}  ')
        return
    else:
        inp_num = inp_num // 10
        reverse_number(inp_num, reverse_str)


def digit_input():
    while True:
        try:
            num = int(input(" please enter an INT  number:   "))
            return num
        except ValueError:
            continue


if __name__ == '__main__':
    number = digit_input()
    reverse_number(number)


# Script listing:
#
#  please enter an INT  number:   12345560
#
#  reverse_num = 06554321

