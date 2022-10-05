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


def num_reverse_cycle(num):
    res = ''
    while True:
        current_num = num % 10
        num = num // 10
        res += str(current_num)
        if num == 0:
            return res


def num_reverse(num):
    current_num = num % 10
    num = num // 10
    if num == 0:
        return current_num
    return str(current_num) + str(num_reverse(num))


if __name__ == "__main__":
    num_to_reverse = int(input("Enter the number to reverse: "))
    print(num_reverse_cycle(num_to_reverse))
    print(num_reverse(num_to_reverse))
