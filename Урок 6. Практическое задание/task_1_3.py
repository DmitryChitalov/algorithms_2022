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

"""
В этой задаче я не учел условие сохранения рекурсии, но такой цели и не было в ДЗ, задача была потратить меньше памяти на выполнение.
Чего я и добился использованием генератора вместо списка.
Задайте длину суммируемого ряда: 1000
Выражение истинно. 500500 == 500500.0
Задайте длину суммируемого ряда: 1400
Выражение истинно. 980700 == 980700.0
Filename: C:\python_projects\Algoritm\lesson_6\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    66     19.4 MiB     19.4 MiB           1   @profile()
    67                                         def for_profile():
    68                                         
    69     22.4 MiB      2.9 MiB        1401       def prove(n=1, lst=[], num=int(input('Задайте длину суммируемого ряда: '))):
    70     22.4 MiB      0.2 MiB        1400           lst.append(n)
    71     22.4 MiB      0.0 MiB        1400           if n == num:
    72     22.4 MiB      0.0 MiB           1               if sum(lst) == n * (n + 1) / 2:
    73     22.4 MiB      0.0 MiB           1                   print(f'Выражение истинно. {sum(lst)} == {n * (n + 1) / 2}')
    74     22.4 MiB      0.0 MiB           1                   return True
    75                                         
    76                                                     else:
    77                                                         print(f'Выражение ложно. {sum(lst)} != {n * (n + 1) / 2}')
    78                                                         return False
    79                                         
    80     22.4 MiB      0.0 MiB        1399           prove(n+1, lst, num)
    81     22.4 MiB      0.0 MiB           1       prove()


Задайте длину суммируемого ряда: 1400
Выражение истинно. 980700.0 == 980700.0
Filename: C:\python_projects\Algoritm\lesson_6\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    87     22.4 MiB     22.4 MiB           1   @profile()
    88                                         def prove_upd(num=int(input('Задайте длину суммируемого ряда: '))):
    89     22.4 MiB      0.0 MiB        2803       gen = (n for n in range(1, num + 1))
    90     22.4 MiB      0.0 MiB           1       a = float(sum(gen))
    91     22.4 MiB      0.0 MiB           1       if a == num * (num + 1) / 2:
    92     22.4 MiB      0.0 MiB           1           print(f'Выражение истинно. {a} == {num * (num + 1) / 2}')
    93     22.4 MiB      0.0 MiB           1           return True
    94                                         
    95                                             else:
    96                                                 print(f'Выражение ложно. {a} != {num * (num + 1) / 2}')
    97                                                 return False

"""

from memory_profiler import profile
import sys

sys.setrecursionlimit(1500)

@profile()
def for_profile():

    def prove(n=1, lst=[], num=int(input('Задайте длину суммируемого ряда: '))):
        lst.append(n)
        if n == num:
            if sum(lst) == n * (n + 1) / 2:
                print(f'Выражение истинно. {sum(lst)} == {n * (n + 1) / 2}')
                del lst
                return True

            else:
                print(f'Выражение ложно. {sum(lst)} != {n * (n + 1) / 2}')
                return False

        prove(n+1, lst, num)
    prove()


for_profile()


@profile()
def prove_upd(num=int(input('Задайте длину суммируемого ряда: '))):
    gen = (n for n in range(1, num + 1))
    a = float(sum(gen))
    if a == num * (num + 1) / 2:
        print(f'Выражение истинно. {a} == {num * (num + 1) / 2}')
        return True

    else:
        print(f'Выражение ложно. {a} != {num * (num + 1) / 2}')
        return False

prove_upd()
