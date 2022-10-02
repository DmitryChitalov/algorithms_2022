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


def proof_set(n, i=0):
    if i == n:
        return 0
    else:
        i += 1
        if i < n:
            print(i, '+ ', end='')
        else:
            print(i, ' ', end='')
        return i + proof_set(n, i)


n = int(input('Введите число элементов множества: '))
result = n * (n + 1) / 2
if proof_set(n) == result:
    print(f'= {n} * ({n} + 1) / 2')
else:
    print(f'Ошибка! {result} = {n}*({n} + 1) / 2')
