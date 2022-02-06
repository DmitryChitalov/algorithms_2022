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

Это файл для пятого скрипта
"""
from json import loads, dumps
from pympler import asizeof

# Алгоритмы, ДЗ-1, task_3
my_dict = {'Comp1': 3500, 'Comp2': 6400, 'Comp3': 84150, 'Comp4': 13800, 'Comp5': 600}

a = list(my_dict.values())
a.sort(reverse=True)

for key, value in my_dict.items():
    if value in a[0:3]:
        print(key)

print(asizeof.asizeof(my_dict))     # 672

# Проведем сериализацию словаря в json-строку
my_dict1 = dumps({'Comp1': 3500, 'Comp2': 6400, 'Comp3': 84150, 'Comp4': 13800, 'Comp5': 600})

a = list(loads(my_dict1).values())  
a.sort(reverse=True)                

for key, value in loads(my_dict1).items(): 
    if value in a[0:3]:            
        print(key)                  


print(asizeof.asizeof(my_dict1))    # 128

# Сериализация словаря позволила уменьшить его объем более, чем в пять раз
