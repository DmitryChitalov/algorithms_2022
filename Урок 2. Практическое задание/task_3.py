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


def rev(num: int):
    if num == 0:
        return "0"
    return rev_rec(num)


def rev_rec(num: int):
    if num == 0:
        return ""
    return f'{num % 10}{rev_rec(num // 10)}'


if __name__ == "__main__":
    tst = [123, 122, 112, 100, 1, 0, 2000, 1234, 123456]
    for ts in tst:
        print(f'{ts} - {rev(ts)}')
