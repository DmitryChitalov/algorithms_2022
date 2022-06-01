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
# Курс Алгоритмы и структуры данных, Урок 2, задание 3
from memory_profiler import profile


@profile
def wrapper(num, reverse_l):
    def reverse(number, reverse_list):
        if number == 0:
            return ''.join(map(str, reverse_list))
        a = number % 10
        reverse_list.append(a)
        return reverse(number//10, reverse_list)
    return reverse(num, reverse_l)


@profile
def reverse_optimized(num):
    reversed_number = ''
    for i in range(num):
        if num == 0:
            return reversed_number
        reversed_number += str(num % 10)
        num //= 10


print(reverse_optimized(9**1000))
print(wrapper(9**1000, []))
print('\nВывод: добился оптимизации памяти превратив рекурсию в цикл и убрав ненужные детали')
