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


def checkexpression(n, i=1, leftSum=0, leftString=''):
    if i > n:
        rightSum = n * (n + 1) / 2
        rightString = f'{n}({n}+1)/2'
        checkResult = '='
        if (rightSum != leftSum):
            checkResult = '!='
        print(leftString + ' ' + checkResult + ' ' + rightString)
        return
    else:
        leftSum += i
        if leftString=='':
            leftString=str(i)
        else:
            leftString = leftString + '+' + str(i)
        return checkexpression(n, i + 1, leftSum, leftString)


n = int(input('Введите n: '))
checkexpression(n)
