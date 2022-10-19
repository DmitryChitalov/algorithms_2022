"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

"""
Основы Python ДЗ_1 задача №2
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
    a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
    b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    c. * Решить задачу под пунктом b, не создавая новый список.


"""

from memory_profiler import profile


# Задача решается по варианту b.
# Первый вариант функция без оптимизации.
@profile
def sum_list_1() -> int:
    dataset = []
    my_list = []
    sum_my_list = 0  # Вводим необходимые для вычисления списки и переменные
    for n in range(1, 100000, 2):
        n = n ** 3 + 17
        dataset.append(n)  # Создаём список кубов нечетных чисел
        sum = 0
        k = n
        while k >= 1:
            sum += k % 10
            k = k // 10
        if sum % 7 == 0:
            my_list.append(n)  # Создаем список сумма чисел членов которого делится на 7
    for indx in my_list:
        sum_my_list += indx  # Вычисляем сумму членов этого списка
    return print(f'Сумма членов списка по заданию вариант а):  {sum_my_list}')  # Верните значение полученной суммы


# Второй вариант функция с оптимизацией.
# Оптимизация следующая: используется list comprehension, сокращено количество циклов, уменьшенно колличество переменных
# и массивов данных, удаление неиспользуемых переменных.

@profile
def sum_list_3() -> int:
    sum_my_list_1 = 0  # Вводим необходимые для вычисления списки и переменные

    for n in [n ** 3 + 17 for n in range(1, 100000, 2)]:
        sum = 0
        k = n
        while k >= 1:
            sum += k % 10
            k = k // 10
        if sum % 7 == 0:
            sum_my_list_1 += n

    return print(f'Сумма членов списка по заданию вариант с):  {sum_my_list_1}')


sum_list_1()
sum_list_3()

"""
В результате оптимизации использования памяти мы получаем:
1. В начале обе функции работали почти одинаково и к завершению их работы объём использованной памяти даже увеличивался 
после завершения работы.
2. После оптимизации, первая работает точно также, зато объём использованной памяти второй(оптимизированной) функции
снижается к концу работы!!! К тому же существенно снизилось количество кода.
Это видно из таблиц профиллирования памяти их работы:

До оптимизациии:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    49     19.4 MiB     19.4 MiB           1   @profile
    50                                         def sum_list_1() -> int:
    51     19.4 MiB      0.0 MiB           1       dataset = []
    52     19.4 MiB      0.0 MiB           1       my_list = []
    53     19.4 MiB      0.0 MiB           1       sum_my_list = 0  # Вводим необходимые для вычисления списки и переменные
    54     22.7 MiB    -13.1 MiB       50001       for n in range(1, 100000, 2):
    55     22.7 MiB    -10.8 MiB       50000           n = n ** 3 + 17
    56     22.7 MiB    -12.4 MiB       50000           dataset.append(n)  # Создаём список кубов нечетных чисел
    57     22.7 MiB    -13.1 MiB       50000           sum = 0
    58     22.7 MiB    -13.1 MiB       50000           k = n
    59     22.7 MiB   -210.5 MiB      756691           while k >= 1:
    60     22.7 MiB   -197.3 MiB      706691               sum += k % 10
    61     22.7 MiB   -197.3 MiB      706691               k = k // 10
    62     22.7 MiB    -13.2 MiB       50000           if sum % 7 == 0:
    63     22.7 MiB     -2.5 MiB        9580               my_list.append(n)  # Создаем список сумма чисел членов которого делится на 7
    64     22.7 MiB      0.0 MiB        9581       for indx in my_list:
    65     22.7 MiB      0.0 MiB        9580           sum_my_list += indx  # Вычисляем сумму членов этого списка
    66     22.7 MiB      0.0 MiB           1       return print(f'Сумма членов списка по заданию вариант а):  {sum_my_list}')

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    73     20.9 MiB     20.9 MiB           1   @profile
    74                                         def sum_list_3() -> int:
    75     20.9 MiB      0.0 MiB           1       dataset = []
    76     20.9 MiB      0.0 MiB           1       sum_my_list_1 = 0  # Вводим необходимые для вычисления списки и переменные
    77     22.3 MiB      0.0 MiB       50001       for n in range(1, 100000, 2):
    78     22.3 MiB      1.0 MiB       50000           n = n ** 3 + 17
    79     22.3 MiB      0.4 MiB       50000           dataset.append(n)  # Создаём список кубов нечетных чисел плюс 17
    80     22.3 MiB   -101.0 MiB       50001       for n in dataset:
    81     22.3 MiB   -101.0 MiB       50000           n = str(n)
    82     22.3 MiB   -101.0 MiB       50000           sum = 0
    83     22.3 MiB  -1616.4 MiB      756691           for i in n:
    84     22.3 MiB  -1515.4 MiB      706691               i = int(i)
    85     22.3 MiB  -1515.4 MiB      706691               sum += i
    86     22.3 MiB   -101.0 MiB       50000           n = int(n)
    87     22.3 MiB   -101.0 MiB       50000           if sum % 7 == 0:
    88     22.3 MiB    -19.8 MiB        9580               sum_my_list_1 += n 
    89
    90     22.2 MiB     -0.0 MiB           1       return print(f'Сумма членов списка по заданию вариант с):  {sum_my_list_1}')
    
После оптимизации:
Функция без изменений.
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    49     19.4 MiB     19.4 MiB           1   @profile
    50                                         def sum_list_1() -> int:
    51     19.4 MiB      0.0 MiB           1       dataset = []
    52     19.4 MiB      0.0 MiB           1       my_list = []
    53     19.4 MiB      0.0 MiB           1       sum_my_list = 0  # Вводим необходимые для вычисления списки и переменные
    54     23.2 MiB    -53.1 MiB       50001       for n in range(1, 100000, 2):
    55     23.2 MiB    -50.8 MiB       50000           n = n ** 3 + 17
    56     23.2 MiB    -51.6 MiB       50000           dataset.append(n)  # Создаём список кубов нечетных чисел
    57     23.2 MiB    -53.1 MiB       50000           sum = 0
    58     23.2 MiB    -53.1 MiB       50000           k = n
    59     23.2 MiB   -850.1 MiB      756691           while k >= 1:
    60     23.2 MiB   -796.9 MiB      706691               sum += k % 10
    61     23.2 MiB   -797.0 MiB      706691               k = k // 10
    62     23.2 MiB    -53.1 MiB       50000           if sum % 7 == 0:
    63     23.2 MiB    -10.9 MiB        9580               my_list.append(n)  # Создаем список сумма чисел членов которого делится на 7
    64     23.2 MiB      0.0 MiB        9581       for indx in my_list:
    65     23.2 MiB      0.0 MiB        9580           sum_my_list += indx  # Вычисляем сумму членов этого списка
    66     23.2 MiB      0.0 MiB           1       return print(f'Сумма членов списка по заданию вариант а):  {sum_my_list}')   # Верните значение полученной суммы

Функция с изменениями.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    73     21.4 MiB     21.4 MiB           1   @profile
    74                                         def sum_list_3() -> int:
    75                                             # dataset = []
    76     21.4 MiB      0.0 MiB           1       sum_my_list_1 = 0  # Вводим необходимые для вычисления списки и переменные
    77                                             # for n in range(1, 100000, 2):
    78                                             #     n = n ** 3 + 17
    79                                             #     dataset.append(n)  # Создаём список кубов нечетных чисел плюс 17
    80                                             #dataset = [n ** 3 + 17 for n in range(1, 100000, 2)]
    81                                         
    82                                             # for n in dataset:
    83                                             #     n = str(n)
    84                                             #     sum = 0
    85                                             #     for i in n:
    86                                             #         i = int(i)
    87                                             #         sum += i
    88                                             #     n = int(n)
    89                                             #     if sum % 7 == 0:
    90                                             #         sum_my_list_1 += n # Вычисляем сумму членов списка, сумма цифр которых делиться нацело на 7
    91     22.1 MiB    -59.7 MiB      100003       for n in [n ** 3 + 17 for n in range(1, 100000, 2)]:
    92     22.1 MiB    -59.0 MiB       50000           sum = 0
    93     22.1 MiB    -59.0 MiB       50000           k = n
    94     22.1 MiB   -943.4 MiB      756691           while k >= 1:
    95     22.1 MiB   -884.5 MiB      706691               sum += k % 10
    96     22.1 MiB   -884.5 MiB      706691               k = k // 10
    97     22.1 MiB    -59.0 MiB       50000           if sum % 7 == 0:
    98     22.1 MiB    -11.5 MiB        9580               sum_my_list_1 += n
    99                                         
   100                                         
   101                                         
   102                                             # for indx in my_list:
   103                                             #     sum_my_list += indx
   104     20.7 MiB     -1.4 MiB           1       return print(f'Сумма членов списка по заданию вариант с):  {sum_my_list_1}')

"""
