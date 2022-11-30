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


def set_of_numbers(n,number,sum):
    if n == 0:
       return (sum)
    else:
       number = number + 1
       sum = sum + number
       n = n - 1
       return(set_of_numbers(n,number,sum))


n = int(input("Введите число: "))
number = 1
sum=0
set_of_numbers(n,number,sum)
if sum == (n*(n+1)/2):
    print('Условие выполнено')
else:
    print('Условие не выполнено')




