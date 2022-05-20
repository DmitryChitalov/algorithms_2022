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

def expression_proof(number, counter=0, summ=0):

    if counter == number:
        return summ

    counter += 1
    summ += counter

    return expression_proof(number=number, counter=counter, summ=summ)


if __name__ == '__main__':

    num = 8
    expression = num * (num + 1)/2
    print('{} = {}'.format(expression_proof(number=num), expression))
