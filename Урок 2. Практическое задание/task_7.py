"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def input_number():
    try:
        number = int(input("Введите натуральное число, которое требуется проверить: "))
    except ValueError:
        print("Неверный формат ввода! Исправьтесь!")
        return input_number()
    return number


def natural_numbers(number):
    """Рекурсивная функция"""
    if number == 1:
        return number
    else:
        return natural_numbers(number - 1) + number


def natural_numbers_ternary(number):
    """Рекурсивная функция, испеользующая тернарный оператор"""
    return number if number == 1 else natural_numbers_ternary(number - 1) + number


if __name__ == "__main__":
    checked_number = input_number()

    if natural_numbers(checked_number) == checked_number * (checked_number + 1) / 2:
        print(f"Равенство 1+2+...+{checked_number} = {checked_number}({checked_number}+1)/2 верно!")
    else:
        print(f"Равенство 1+2+...+{checked_number} = {checked_number}({checked_number}+1)/2 не верно!")

    if natural_numbers_ternary(checked_number) == checked_number * (checked_number + 1) / 2:
        print(f"Равенство 1+2+...+{checked_number} = {checked_number}({checked_number}+1)/2 верно!")
    else:
        print(f"Равенство 1+2+...+{checked_number} = {checked_number}({checked_number}+1)/2 не верно!")
