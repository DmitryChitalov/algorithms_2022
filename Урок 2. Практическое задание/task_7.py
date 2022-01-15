"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""

def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)

def check_equality(amounts_elements):
    def sum_range(amounts_elements, current_number = 1):
        if amounts_elements == current_number:
            return current_number
        return current_number + sum_range(amounts_elements, current_number+1)
    return sum_range(amounts_elements) == amounts_elements*(amounts_elements+1)/2
    
print(check_equality(30))