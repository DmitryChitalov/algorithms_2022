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

Это файл для третьего скрипта
"""

from memory_profiler import profile



# my_list = [3, 5, 7, 9, 11, 2, 13, 15]  # O(1)

# @profile
# def min_lst_func2(lst):
#     my_min = lst[0]  # O(1)
#     for i in range(len(lst)):  # O(n)
#         for j in range(len(lst)):  # O(n)
#             if my_min > lst[j]:  # 0(1)
#                 my_min = lst[j]  # 0(1)
#     return my_min  # O(1)
#
#
# print(min_lst_func2(my_list))



@profile
def min_lst_func2():
    my_list = (3, 5, 7, 9, 11, 2, 13, 15)
    my_min = my_list[0]  # O(1)
    for i in range(len(my_list)):  # O(n)
        for j in range(len(my_list)):  # O(n)
            if my_min > my_list[j]:  # 0(1)
                my_min = my_list[j]  # 0(1)
    print(f'{my_min}')  # O(1)
    del my_min
    del my_list


min_lst_func2()

"""
Самое главное тут, что список заменен на кортеж...+ опять же удалены переменные и добавлена f-строка.

"""