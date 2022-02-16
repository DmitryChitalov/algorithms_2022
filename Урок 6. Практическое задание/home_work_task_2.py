from memory_profiler import profile

'''
Первая часть задания: профилирование памяти в скрипте с рекурсией: расчет факториала.
Проблема, в том, что профилирование памяти производится n раз.
А объем памяти сильно не меняется.
'''


@profile
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

'''
Идею обернуть рекурсивную функцию в другую функцию взяла из подсказки.
Профилирование памяти тогда считается 1 раз.
'''


@profile
def wrapper(input_number):
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)

    return factorial(input_number)


print(wrapper(5))

'''
n = 1
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     13.2 MiB     13.2 MiB           1   @profile
     5                                         def factorial(n):
     6     13.2 MiB      0.0 MiB           1       if n <= 1:
     7     13.2 MiB      0.0 MiB           1           return 1
     8                                             else:
     9                                                 return n * factorial(n - 1)
1

n = 3
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     13.3 MiB     13.3 MiB           1   @profile
     5                                         def factorial(n):
     6     13.3 MiB      0.0 MiB           1       if n <= 1:
     7     13.3 MiB      0.0 MiB           1           return 1
     8                                             else:
     9                                                 return n * factorial(n - 1)


Filename: /Users/svetlanakargasinskaya/PycharmProjects/algorithms_2022/Урок 6. Практическое задание/home_work_task_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     13.3 MiB     13.3 MiB           2   @profile
     5                                         def factorial(n):
     6     13.3 MiB      0.0 MiB           2       if n <= 1:
     7     13.3 MiB      0.0 MiB           1           return 1
     8                                             else:
     9     13.3 MiB      0.0 MiB           1           return n * factorial(n - 1)


Filename: /Users/svetlanakargasinskaya/PycharmProjects/algorithms_2022/Урок 6. Практическое задание/home_work_task_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     13.3 MiB     13.3 MiB           3   @profile
     5                                         def factorial(n):
     6     13.3 MiB      0.0 MiB           3       if n <= 1:
     7     13.3 MiB      0.0 MiB           1           return 1
     8                                             else:
     9     13.3 MiB      0.0 MiB           2           return n * factorial(n - 1)
6


n = 15 (размещаю здесь последний замер памяти):
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     13.3 MiB     13.3 MiB          15   @profile
     5                                         def factorial(n):
     6     13.3 MiB      0.0 MiB          15       if n <= 1:
     7     13.3 MiB      0.0 MiB           1           return 1
     8                                             else:
     9     13.3 MiB      0.0 MiB          14           return n * factorial(n - 1)

1307674368000


n = 115 (размещаю здесь последний замер памяти):
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     14.2 MiB     14.2 MiB         115   @profile
     5                                         def factorial(n):
     6     14.2 MiB      0.0 MiB         115       if n <= 1:
     7     14.2 MiB      0.0 MiB           1           return 1
     8                                             else:
     9     14.3 MiB      0.0 MiB         114           return n * factorial(n - 1)


292509369349301569068815180481773552003419272043053514672100535242441942363589054622883930786268803187059211939585703515345785120071002251720730101703194015956992000000000000000000000000000



После того, как обернула рекурсивную функцию в другую функцию - замер памяти производится 1 раз, 
независимо от  input_number.
input_number = 5 Профилировка памяти производится 1 раз.
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     13.4 MiB     13.4 MiB           1   @profile
    16                                         def wrapper(input_number):
    17     13.4 MiB      0.0 MiB           6       def factorial(n):
    18     13.4 MiB      0.0 MiB           5           if n <= 1:
    19     13.4 MiB      0.0 MiB           1               return 1
    20                                                 else:
    21     13.4 MiB      0.0 MiB           4               return n * factorial(n - 1)
    22     13.4 MiB      0.0 MiB           1       return factorial(input_number)


120
'''
