"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections
from collections import defaultdict, namedtuple
import pickle
from memory_profiler import profile
from pympler import asizeof
from memory_profiler import memory_usage
from time import time



#@profile
def check():
    try:
        count_company = int(input('введите колличество компаний '))
        cmp = count_company # делитель отелён от кол-ва компаний, чтоб потом найти среднее значение прибыли всех к-ий
    except ValueError:
        print('введите число')
        return check()
    d_1 = defaultdict(float)
    max_val = []
    min_val = []
    while count_company > 0:
        company = input('введите название компании ')
        try:
            s = sum(list(map(int, input('введите прибыль за каждый квартал '
                                        'через пробел(всего 4 квартала) ').split(' ')))) / 4
            d_1[company] = s
            count_company -= 1
        except ValueError:
            print('введите число')
            return check()
    average_sum_cmp = sum(d_1.values()) / cmp
    for i, v in d_1.items():
        if v > average_sum_cmp:
            max_val.append(i)
        elif v < average_sum_cmp:
            min_val.append(i)
    return max_val, min_val, average_sum_cmp


#max_val, min_val, average_sum_cmp = check()
#print('Предприятия, с прибылью выше среднего значения: ', ', '.join(max_val),
#      'Предприятия, с прибылью ниже среднего значения: ', ', '.join(min_val),
#      'средняя прибыль всех предприятий за год:', average_sum_cmp, sep='\n')
#print(asizeof.asizeof(max_val, min_val, average_sum_cmp))


#@profile
def check_2():
    try:
        count_company = int(input('введите колличество компаний '))
        cmp = count_company # делитель отелён от кол-ва компаний, чтоб потом найти среднее значение прибыли всех к-ий
    except ValueError:
        print('введите число')
        return check()
    d_1 = defaultdict(float)
    while count_company > 0:
        company = input('введите название компании ')
        try:
            d_1[company] = sum(list(map(int, input('введите прибыль за каждый квартал '
                                        'через пробел(всего 4 квартала) ').split(' ')))) / 4
            count_company -= 1
        except ValueError:
            print('введите число')
            return check()
    average_sum_cmp = sum(d_1.values()) / cmp
    max_val = pickle.dumps([i for i, v in d_1.items() if v > average_sum_cmp])
    min_val = pickle.dumps([i for i, v in d_1.items() if v < average_sum_cmp])
    return max_val, min_val, average_sum_cmp


#max_val, min_val, average_sum_cmp = check_2()
#print('Предприятия, с прибылью выше среднего значения: ', pickle.loads(max_val),
#      'Предприятия, с прибылью ниже среднего значения: ', pickle.loads(min_val),
#      'средняя прибыль всех предприятий за год:', average_sum_cmp, sep='\n')
#print(asizeof.asizeof(max_val, min_val, average_sum_cmp))




'''АНАЛИТИКА
Оптимизировал функцию check c помощью list comprehension и сериализацией списков с помощью pickle
check: 208 общий размер занимаемой памяти asizeof 
check_2: 104 общий размер занимаемой памяти asizeof

Функция check

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     26.1 MiB     26.1 MiB           1   @profile
    33                                         def check():
    34     26.1 MiB      0.0 MiB           1       try:
    35     26.1 MiB      0.0 MiB           1           count_company = int(input('введите колличество компаний '))
    36     26.1 MiB      0.0 MiB           1           cmp = count_company
    37                                             except ValueError:
    38                                                 print('введите число')
    39                                                 return check()
    40     26.1 MiB      0.0 MiB           1       d_1 = defaultdict(float)
    41     26.1 MiB      0.0 MiB           1       max_val = []
    42     26.1 MiB      0.0 MiB           1       min_val = []
    43     26.1 MiB      0.0 MiB           4       while count_company > 0:
    44     26.1 MiB      0.0 MiB           3           company = input('введите название компании ')
    45     26.1 MiB      0.0 MiB           3           try:
    46     26.1 MiB      0.0 MiB           9               s = sum(list(map(int, input('введите прибыль за каждый квартал '
    47     26.1 MiB      0.0 MiB           6                                           'через пробел(всего 4 квартала) ').split(' ')))) / 4
    48     26.1 MiB      0.0 MiB           3               d_1[company] = s
    49     26.1 MiB      0.0 MiB           3               count_company -= 1
    50                                                 except ValueError:
    51                                                     print('введите число')
    52                                                     return check()
    53     26.1 MiB      0.0 MiB           1       average_sum_cmp = sum(d_1.values()) / cmp
    54     26.1 MiB      0.0 MiB           4       for i, v in d_1.items():
    55     26.1 MiB      0.0 MiB           3           if v > average_sum_cmp:
    56     26.1 MiB      0.0 MiB           1               max_val.append(i)
    57     26.1 MiB      0.0 MiB           2           elif v < average_sum_cmp:
    58     26.1 MiB      0.0 MiB           2               min_val.append(i)
    59     26.1 MiB      0.0 MiB           1       return max_val, min_val, average_sum_cmp


Предприятия, с прибылью выше среднего значения: 
q
Предприятия, с прибылью ниже среднего значения: 
e, w
средняя прибыль всех предприятий за год:
17.5
208 размер занимаемой памяти sizeof

Функция check_2

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     26.1 MiB     26.1 MiB           1   @profile
    69                                         def check_2():
    70     26.1 MiB      0.0 MiB           1       try:
    71     26.1 MiB      0.1 MiB           1           count_company = int(input('введите колличество компаний '))
    72     26.1 MiB      0.0 MiB           1           cmp = count_company # делитель отелён от кол-ва компаний, чтоб потом найти среднее значение прибыли всех к-ий
    73                                             except ValueError:
    74                                                 print('введите число')
    75                                                 return check()
    76     26.1 MiB      0.0 MiB           1       d_1 = defaultdict(float)
    77     26.1 MiB      0.0 MiB           4       while count_company > 0:
    78     26.1 MiB      0.0 MiB           3           company = input('введите название компании ')
    79     26.1 MiB      0.0 MiB           3           try:
    80     26.1 MiB      0.0 MiB           9               d_1[company] = sum(list(map(int, input('введите прибыль за каждый квартал '
    81     26.1 MiB      0.0 MiB           6                                           'через пробел(всего 4 квартала) ').split(' ')))) / 4
    82     26.1 MiB      0.0 MiB           3               count_company -= 1
    83                                                 except ValueError:
    84                                                     print('введите число')
    85                                                     return check()
    86     26.1 MiB      0.0 MiB           1       average_sum_cmp = sum(d_1.values()) / cmp
    87     26.1 MiB      0.0 MiB           6       max_val = pickle.dumps([i for i, v in d_1.items() if v > average_sum_cmp])
    88     26.1 MiB      0.0 MiB           6       min_val = pickle.dumps([i for i, v in d_1.items() if v < average_sum_cmp])
    89                                             #return ''.join(max_val), ''.join(min_val), average_sum_cmp
    90     26.1 MiB      0.0 MiB           1       return max_val, min_val, average_sum_cmp
    
'''


