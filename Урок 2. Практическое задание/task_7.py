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

# Задание № 7


def func_equality(user_number, result=0, formula=0):
    if formula == 0:
        formula = user_number
        return func_equality(user_number, result, formula)
    else:
        if user_number > 0:
            result += user_number
            user_number -= 1
            return func_equality(user_number, result, formula)
        elif result == formula * (formula + 1) / 2:
            print(f'Сумма 1+2+...{formula} равна: {result}, Расчет по формуле {formula}*({formula}+1)/2, равен: {result}')
            print("Формула : 1+2+...+n = n(n+1)/2")


func_equality(user_number=int(input("Введите число: ")))
