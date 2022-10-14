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

# Урок 1 задание 2 Основы
from memory_profiler import profile

@profile
def sum_cub():
    lc = []
    for i in range(1, 1000, 2):
        lc.append(i ** 3)
    sumNum = 0
    for i in lc:
        sum = 0
        for j in str(i):
            sum += int(j)
        if (sum % 7) == 0:
            sumNum += i

    print(sumNum)

@profile
def sum_cub_opt():
    lc = (i ** 3 for i in range(1, 1000, 2))
    sumNum = 0
    for i in lc:
        sum = 0
        for j in str(i):
            sum += int(j)
        if (sum % 7) == 0:
            sumNum += i
    # Удалим уже ненужную переменную
    del sum
    del lc
    print(sumNum)

sum_cub()
# С использованием генератора
sum_cub_opt()