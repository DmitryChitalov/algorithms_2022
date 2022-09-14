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

from memory_profiler import profile, memory_usage

# Курс Основы Python lesson_2 task_3

# До оптимизации


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(args[0], **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Общий размер: {mem_diff}')
    return wrapper


@decor
@profile
def corrected(data):
    for element in data:
        employee_info = element.split()
        name_employee = employee_info[len(employee_info) - 1]
        correct_name = name_employee.capitalize()
        print(f'Привет {correct_name}')


list_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

corrected(list_employees)

# После оптимизации


@decor
@profile
def corrected(data):
    for element in data:
        employee_info = element.split()
        name_employee = employee_info[len(employee_info) - 1]
        correct_name = name_employee.capitalize()
        print(f'Привет {correct_name}')


list_employees = ('инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита')

corrected(list_employees)
del list_employees

"""
Вместо списка используем кортеж и показатели по общему
расходу памяти снижаются,в данном скрипте не намного, но при большем размере
данных, будет существенная разница

Общий размер до оптимизации: 0.30078125 
Общий размер после оптимизации: 0.0

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     19.3 MiB     19.3 MiB           1   @profile
    41                                         def corrected(data):
    42     19.4 MiB      0.0 MiB           5       for element in data:
    43     19.4 MiB      0.0 MiB           4           employee_info = element.split()
    44     19.4 MiB      0.0 MiB           4           name_employee = employee_info[len(employee_info) - 1]
    45     19.4 MiB      0.0 MiB           4           correct_name = name_employee.capitalize()
    46     19.4 MiB      0.0 MiB           4           print(f'Привет {correct_name}')
    
    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    58     19.3 MiB     19.3 MiB           1   @profile
    59                                         def corrected(data):
    60     19.3 MiB      0.0 MiB           5       for element in data:
    61     19.3 MiB      0.0 MiB           4           employee_info = element.split()
    62     19.3 MiB      0.0 MiB           4           name_employee = employee_info[len(employee_info) - 1]
    63     19.3 MiB      0.0 MiB           4           correct_name = name_employee.capitalize()
    64     19.3 MiB      0.0 MiB           4           print(f'Привет {correct_name}')
"""
