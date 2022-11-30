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

def summa(count,element,sum):
    if count == 0:
        return(sum)
    else:
        sum = sum + element
        element = element / -2
        count = count - 1
        return (summa(count,element,sum))


count=int(input('Введите количество чисел в ряду: '))
element=-0.5
sum=0
print(summa(count,element,sum))