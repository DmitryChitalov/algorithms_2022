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


def input_length():
    try:
        length = int(input("Введите количество элементов: "))
    except ValueError:
        print("Неверный формат ввода! Исправьтесь!")
        return input_length()
    return length


def sum_of_elements(count, number, length, total):
    """Рекурсивная функция"""
    if count == length:
        print(f"Количество элементов - {length}, их сумма - {total}")
    elif count < length:
        return sum_of_elements(count + 1, number/2 * -1, length, total + number)


if __name__ == "__main__":
    sum_of_elements(0, 1, input_length(), 0)
