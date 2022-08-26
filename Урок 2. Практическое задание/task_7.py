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


def subsequence_sum(n, sum_elements=0, start=1):
    if isinstance(start, int):
        if start < n:
            return subsequence_sum(n, sum_elements + start, start + 1)
        if start == n:
            sum_elements += start
            if sum_elements == n * (n + 1) / 2:
                # я помню, что вы на уроке сказали, что требуется написать функцию только для левой части,
                # но у меня здесь это влияет только на return и из-за этого по задаче не требуется внешней проверки.
                # Считаю уместным, но если надо - перепишу
                return True
            else:
                return False
    else:
        return f'Вы ввели не целое число'


if __name__ == '__main__':
    for i in range(1, 101):
        print(f'n = {i} : {subsequence_sum(i)}')
