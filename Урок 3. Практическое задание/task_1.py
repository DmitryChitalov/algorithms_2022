"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что выполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что выполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что выполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

# Python 3.9.2
import dis
from time import time

times = 10 ** 7
print("times", times)

def exec_time(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed: {end - start}')
        return result
    return timer
print("----------------------------------")
# List
@exec_time
def list_append(list):
    for x in range(0, times):
        list.append(1000) # O(1)
    return list

@exec_time
def list_insert(list):
    print("list_insert - смысла замерять, ужасная крайне функция")
    return list
    # for x in range(0, times):
        # list.insert(0, 1000) # O(n)
    # return list

list_append([])
list_insert([])

# Dict
@exec_time
def dict_dict(dict):
    for x in range(0, times):
        dict[x] = 1000 # O(1)
    return dict

dict_dict({})

dis.dis(list_append)
print('------------')
dis.dis(dict_dict)
"""
# List.append быстрее. 
Список не создает хэши, из-за чего происходит добавление быстрее чем словаре
times 10000000
----------------------------------
list_append executed: 0.8666300773620605
list_insert - смысла замерять, ужасная крайне функция
list_insert executed: 0.0
dict_dict executed: 0.9160425662994385
 39           0 LOAD_GLOBAL              0 (time)
              2 CALL_FUNCTION            0
              4 STORE_FAST               2 (start)

 40           6 LOAD_DEREF               0 (func)
              8 LOAD_FAST                0 (args)
             10 LOAD_FAST                1 (kwargs)
             12 CALL_FUNCTION_EX         1
             14 STORE_FAST               3 (result)

 41          16 LOAD_GLOBAL              0 (time)
             18 CALL_FUNCTION            0
             20 STORE_FAST               4 (end)

 42          22 LOAD_GLOBAL              1 (print)
             24 LOAD_DEREF               0 (func)
             26 LOAD_ATTR                2 (__name__)
             28 FORMAT_VALUE             0
             30 LOAD_CONST               1 (' executed: ')
             32 LOAD_FAST                4 (end)
             34 LOAD_FAST                2 (start)
             36 BINARY_SUBTRACT
             38 FORMAT_VALUE             0
             40 BUILD_STRING             3
             42 CALL_FUNCTION            1
             44 POP_TOP

 43          46 LOAD_FAST                3 (result)
             48 RETURN_VALUE
------------
 39           0 LOAD_GLOBAL              0 (time)
              2 CALL_FUNCTION            0
              4 STORE_FAST               2 (start)

 40           6 LOAD_DEREF               0 (func)
              8 LOAD_FAST                0 (args)
             10 LOAD_FAST                1 (kwargs)
             12 CALL_FUNCTION_EX         1
             14 STORE_FAST               3 (result)

 41          16 LOAD_GLOBAL              0 (time)
             18 CALL_FUNCTION            0
             20 STORE_FAST               4 (end)

 42          22 LOAD_GLOBAL              1 (print)
             24 LOAD_DEREF               0 (func)
             26 LOAD_ATTR                2 (__name__)
             28 FORMAT_VALUE             0
             30 LOAD_CONST               1 (' executed: ')
             32 LOAD_FAST                4 (end)
             34 LOAD_FAST                2 (start)
             36 BINARY_SUBTRACT
             38 FORMAT_VALUE             0
             40 BUILD_STRING             3
             42 CALL_FUNCTION            1
             44 POP_TOP

 43          46 LOAD_FAST                3 (result)
             48 RETURN_VALUE
"""

print("----------------------------------")
# List O(1)
@exec_time
def get_list(list):
    for x in range(0, times):
        x = list[x] # O(1)

# Dict O(1)
@exec_time
def get_dict(dict):
    for x in range(0, times):
        x = dict[x] # O(1)

dict = {}
for x in range(0, times):
    dict[x] = 1000
get_list([x for x in range(0, times)])
get_dict(dict)

print('------------')
dis.dis(get_list)
print('------------')
dis.dis(get_dict)
"""
# List[index] быстрее.
Доступ к элементам в массиве происходит быстрее, чем вычисление хэша
get_list executed: 0.3515281677246094
get_dict executed: 0.4787900447845459
------------
 39           0 LOAD_GLOBAL              0 (time)
              2 CALL_FUNCTION            0
              4 STORE_FAST               2 (start)

 40           6 LOAD_DEREF               0 (func)
              8 LOAD_FAST                0 (args)
             10 LOAD_FAST                1 (kwargs)
             12 CALL_FUNCTION_EX         1
             14 STORE_FAST               3 (result)

 41          16 LOAD_GLOBAL              0 (time)
             18 CALL_FUNCTION            0
             20 STORE_FAST               4 (end)

 42          22 LOAD_GLOBAL              1 (print)
             24 LOAD_DEREF               0 (func)
             26 LOAD_ATTR                2 (__name__)
             28 FORMAT_VALUE             0
             30 LOAD_CONST               1 (' executed: ')
             32 LOAD_FAST                4 (end)
             34 LOAD_FAST                2 (start)
             36 BINARY_SUBTRACT
             38 FORMAT_VALUE             0
             40 BUILD_STRING             3
             42 CALL_FUNCTION            1
             44 POP_TOP

 43          46 LOAD_FAST                3 (result)
             48 RETURN_VALUE
------------
 39           0 LOAD_GLOBAL              0 (time)
              2 CALL_FUNCTION            0
              4 STORE_FAST               2 (start)

 40           6 LOAD_DEREF               0 (func)
              8 LOAD_FAST                0 (args)
             10 LOAD_FAST                1 (kwargs)
             12 CALL_FUNCTION_EX         1
             14 STORE_FAST               3 (result)

 41          16 LOAD_GLOBAL              0 (time)
             18 CALL_FUNCTION            0
             20 STORE_FAST               4 (end)

 42          22 LOAD_GLOBAL              1 (print)
             24 LOAD_DEREF               0 (func)
             26 LOAD_ATTR                2 (__name__)
             28 FORMAT_VALUE             0
             30 LOAD_CONST               1 (' executed: ')
             32 LOAD_FAST                4 (end)
             34 LOAD_FAST                2 (start)
             36 BINARY_SUBTRACT
             38 FORMAT_VALUE             0
             40 BUILD_STRING             3
             42 CALL_FUNCTION            1
             44 POP_TOP

 43          46 LOAD_FAST                3 (result)
             48 RETURN_VALUE

Process finished with exit code 0

"""
@exec_time
def remove_list(list: list):
    for x in range(0, times):
        list.pop()

@exec_time
def remove_dict(dict: dict):
    for x in range(0, times):
        dict.pop(x)

dict = {}
for x in range(0, times):
    dict[x] = 1000
remove_list([x for x in range(0, times)])
remove_dict(dict)

"""
List.pop быстрее.
Хэш таблицы нужны для поиска

remove_list executed: 0.8500466346740723
remove_dict executed: 1.2507882118225098

remove_list executed: 0.8419754505157471
remove_dict executed: 1.2408678531646729
"""