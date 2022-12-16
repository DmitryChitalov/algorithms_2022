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
from random import randint
from timeit import timeit


# Классический вариант
def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


my_array = [randint(-100, 100) for _ in range(10)]
print('исходный массив:', my_array)

# замер 10: 0.014546700003847945
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(100)]
print('исходный массив:', my_array)

# замер 100: 0.9264003000062075
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(200)]
print('исходный массив:', my_array)

# замер 200: 3.9482208999979775
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')


# Оптимизированный вариант

def bubble_sort_optimize(my_list):
    n = 1
    while n < len(my_list):
        counter = 0
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                counter += 1
        if counter == 0:
            break
        n += 1
    return my_list


my_array = [randint(-100, 100) for _ in range(10)]
print('исходный массив:', my_array)

# замер 10:  0.010672199998225551
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(100)]
print('исходный массив:', my_array)

# замер 100: 1.0987595000042347
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(200)]
print('исходный массив:', my_array)

# замер 200: 4.340785799999139
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

# Вывод: доработанный алгоритм в целом работает немного медленнее, чем классический, потому что в него добавлен
# счетчик и дополнительная проверка. Но когда функции передается уже отсортированный массив, доработанный алгоритм
# это распознает и не делает лишние операции по сортировке, поэтому выполнится значительно быстрее.