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

Это файл для второго скрипта

Algorithms 5_3

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее


3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

script listing приложен ниже кода

Аналитика: сравнивалось потребление памяти при организации списков в виде list и deque
на основании распечаток ниже операции с List более затратные чем операции с Deque

# running : append_list             # Выполнение заняло 4.80859375 Mib
# running : append_deque            # Выполнение заняло 3.1953125 Mib

running : extend_list               Выполнение заняло 1.015625 Mib
running : extend_deque              Выполнение заняло -0.00390625 Mib

running : insert_list               Выполнение заняло 1.109375 Mib
running : append_left_deque         Выполнение заняло 0.359375 Mib

running : pop_left_list             Выполнение заняло 0.00390625 Mib
running : pop_left_deque            Выполнение заняло 0.0 Mib


"""
from collections import deque
from memory_profiler import memory_usage
from memory_profiler import profile



def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def append_list():
    print(f'running : append_list')
    gen_lst = []
    for i in range(100000):
        gen_lst.append(i)
    return gen_lst


@memory
def append_deque():
    print(f'running : append_deque')
    gen_deq = deque([])
    for i in range(100000):
        gen_deq.append(i)
    return gen_deq


def append_list1():
    print(f'running : append_list')
    gen_lst = []
    for i in range(100000):
        gen_lst.append(i)
    return gen_lst


def append_deque1():
    print(f'running : append_deque')
    gen_deq = deque([])
    for i in range(100000):
        gen_deq.append(i)
    return gen_deq


@memory
def pop_list(inp_list):
    print(f'running : pop_list')
    while inp_list:
        a = inp_list.pop()

@memory
def pop_deque(inp_deq):
    print(f'running : pop_deque')
    while inp_deq:
        a = inp_deq.pop()


@memory
def extend_list(inp_list):
    print(f'running : extend_list')
    for i in range(10000):
        inp_list.extend(['a', 'b', 'c'])
    return


@memory
def extend_deque(inp_deq):
    print(f'running : extend_deque')
    for i in range(10000):
        inp_deq.extend(['a', 'b', 'c'])
    return

@memory
def insert_list(inp_list):
    print(f'running : insert_list')
    for i in range(10000):
        inp_list.insert(0, i)
    return

@memory
def append_left_deque(inp_deq):
    print(f'running : append_left_deque')
    for i in range(10000):
        inp_deq.appendleft(i)
    return

@memory
def pop_left_list(inp_list):
    print(f'running : pop_left_list')
    while inp_list:
        a = inp_list.pop(0)
    return

@memory
def pop_left_deque(inp_deq):
    print(f'running : pop_left_deque')
    while inp_deq:
        a = inp_deq.popleft()
    return

@memory
def extend_left_list(inp_list):
    print(f'running : extend_left_list')
    for i in range(10000):
        for j in ['a', 'b', 'c']:
            inp_list.insert(0, j)
    return

@memory
def extend_left_deque(inp_deq):
    print(f'running : extend_left_deque')
    for i in range(10000):
        inp_deq.extendleft(['a', 'b', 'c'])
    return

@memory
def get_from_list(inp_list):
    print(f'running : get_from_list')
    for i in range(10000):
        a = inp_list[i]
    return a

@memory
def get_from_deque(inp_deq):
    print(f'running : get_from_deque')
    for i in range (10000):
        a = inp_deq[i]
    return a




print(f'\n ---- Memory Measurements ---- ')

print('')
inp_list1 = append_list()
inp_deq1 = append_deque()
print('')
inp_list2 = append_list1()
inp_deq2 = append_deque1()
pop_list(inp_list2)
pop_deque(inp_deq2)
print('')
inp_list3 = append_list1()
inp_deq3 = append_deque1()
extend_list(inp_list3)
extend_deque(inp_deq3)
print('')
inp_list4 = append_list1()
inp_deq4 = append_deque1()
insert_list(inp_list4)
append_left_deque(inp_deq4)
print('')
inp_list5 = append_list1()
inp_deq5 = append_deque1()
pop_left_list(inp_list2)
pop_left_deque(inp_deq2)
print('')
inp_list6 = append_list1()
inp_deq6 = append_deque1()
extend_left_list(inp_list6)
extend_left_deque(inp_deq6)
print('')
inp_list7 = append_list1()
inp_deq7 = append_deque1()
get_from_list(inp_list7)
get_from_deque(inp_deq7)

# Script listing:
#
#
#  ---- Memory Measurements ----
#
# running : append_list
# Выполнение заняло 4.80859375 Mib
# running : append_deque
# Выполнение заняло 3.1953125 Mib
#
# running : append_list
# running : append_deque
# running : pop_list
# Выполнение заняло -2.5 Mib
# running : pop_deque
# Выполнение заняло -4.3359375 Mib
#
# running : append_list
# running : append_deque
# running : extend_list
# Выполнение заняло 1.015625 Mib
# running : extend_deque
# Выполнение заняло -0.00390625 Mib
#
# running : append_list
# running : append_deque
# running : insert_list
# Выполнение заняло 1.109375 Mib
# running : append_left_deque
# Выполнение заняло 0.359375 Mib
#
# running : append_list
# running : append_deque
# running : pop_left_list
# Выполнение заняло 0.00390625 Mib
# running : pop_left_deque
# Выполнение заняло 0.0 Mib
#
# running : append_list
# running : append_deque
# running : extend_left_list
# Выполнение заняло 0.22265625 Mib
# running : extend_left_deque
# Выполнение заняло 0.2578125 Mib
#
# running : append_list
# running : append_deque
# running : get_from_list
# Выполнение заняло 0.0 Mib
# running : get_from_deque
# Выполнение заняло 0.00390625 Mib
#
# Process finished with exit code 0
