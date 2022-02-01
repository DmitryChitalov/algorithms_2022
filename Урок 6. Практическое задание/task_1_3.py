"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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
# Дано 1000 точек на плоскости. Найти три точки, которые дают максимальную площадь.
# ============= Итоги ==============
# Первоначальный вариант:
# Расход памяти: 2.8945 MiB
# С dataobject: 1.0312 MiB
# Объекты из библиотеки recordclass являются облегченными, 
# поэтому требуют меньше оперативной памяти

# ====== Генерация точек ===========
from random import randint
from memory_profiler import profile
from recordclass import dataobject


# @profile(precision=4)
def foo():
    point_list = [{'x': randint(0, 10**6) ,'y': randint(0, 10**6)} 
                    for _ in range(10000)]
    s_max = 0
    points_with_max_s = {}
    for num_p1 in range(10):
        for num_p2 in range(10):
            for num_p3 in range(10):
                x1 = point_list[num_p1]['x']
                x2 = point_list[num_p2]['x']
                x3 = point_list[num_p3]['x']
                y1 = point_list[num_p1]['y']
                y2 = point_list[num_p2]['y']
                y3 = point_list[num_p3]['y']
                s = 1/2*abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
                if s_max < s:
                    s_max = s
                    points_with_max_s['p1'] = (x1, y1)
                    points_with_max_s['p2'] = (x2, y2)
                    points_with_max_s['p3'] = (x3, y3)
    return points_with_max_s


@profile(precision=4)
def foo2():
    class Point(dataobject):
        x:int
        y:int
    point_list = [Point(randint(10**6, 2*10**6), randint(2*10**6, 3*10**6))
                 for _ in range(10000)]
    s_max = 0
    points_with_max_s = {}
    for num_p1 in range(10):
        for num_p2 in range(10):
            for num_p3 in range(10):
                x1 = point_list[num_p1].x
                x2 = point_list[num_p2].x
                x3 = point_list[num_p3].x
                y1 = point_list[num_p1].y
                y2 = point_list[num_p2].y
                y3 = point_list[num_p3].y
                s = 1/2*abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
                if s_max < s:
                    s_max = s
                    points_with_max_s['p1'] = (x1, y1)
                    points_with_max_s['p2'] = (x2, y2)
                    points_with_max_s['p3'] = (x3, y3)
    return points_with_max_s

foo2()
