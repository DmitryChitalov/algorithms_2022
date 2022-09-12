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
"""
from pympler import asizeof
from numpy import array

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В']

def generator_tutors(tutors, groups):
    length = len(groups)
    for idx, man in enumerate(tutors):
        if idx < length:
            yield man, groups[idx]
        else:
            yield man, None

gen_tutors = generator_tutors(tutors, groups)
for _ in range(len(tutors)):
    print(next(gen_tutors))

print(asizeof.asizeof(generator_tutors(tutors, groups)))

# после оптимизации
tutors_o = array(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'])
groups_o = array(['9А', '7В', '9Б', '9В'])

def generator_tutors_o(tutors, groups):
    length = len(groups)
    for idx, man in enumerate(tutors):
        if idx < length:
            yield man, groups[idx]
        else:
            yield man, None
gen_tutors = generator_tutors_o(tutors, groups)
for _ in range(len(tutors)):
    print(next(gen_tutors))

print(asizeof.asizeof(generator_tutors_o(tutors_o, groups_o)))
# Использование array сократило использование памяти почти в 2 раза (до 1600 после 984)