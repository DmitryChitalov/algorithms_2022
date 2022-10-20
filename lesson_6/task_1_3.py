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
from numpy import array
import numpy as np
from pympler import asizeof

'''За основу взято задание 5.4 Основы питона, "Представлен список чисел. Необходимо вывести те его элементы, 
значения которых больше предыдущего". 
Для оптимизации используется numpy библиотека, а именно будем преобразовывать список в array. Замеры сделаны с помощью
pympler. Произведенные замеры показывают, что результирующий список в первом случае составляет 404584, в варианте с 
array - 404584, т.е. разница составила в 10 раз в пользу numpy - array!
'''


# было:
def list_more_numb_1(lst):
    result = [num for i, num in enumerate(lst) if lst[i] > lst[i - 1] and i > 0]
    return result


# стало:
def list_more_numb_2(lst):
    result = array([num for i, num in enumerate(lst) if lst[i] > lst[i - 1] and i > 0])
    return result


some_list = np.random.randint(0, 300, 20000)

result = [num for i, num in enumerate(some_list) if some_list[i] > some_list[i - 1] and i > 0]  # результирующий список
# с базового варианта домашней работы
print(asizeof.asizeof(result))  # => 404584

# вариант с array
result = array([num for i, num in enumerate(some_list) if some_list[i] > some_list[i - 1] and i > 0])
print(asizeof.asizeof(result))  # => 40056