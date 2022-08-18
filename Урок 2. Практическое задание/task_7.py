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


def get_proof_form(num):
    num_cur = num
    if num_cur == 1:
        return num_cur
    else:
        return num_cur + get_proof_form(num_cur - 1)


first_num = int(input("Введите натуральное число:  "))
first_sum = int(first_num * (first_num + 1) / 2)
last_sum = get_proof_form(first_num)
if first_sum == last_sum:
    print(f"Все сходится: {first_sum} = {last_sum}")
else:
    print(f"Что-то не так: {first_sum} не равно {last_sum}")
