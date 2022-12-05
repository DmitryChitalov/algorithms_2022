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
from sys import getsizeof
from memory_profiler import profile


"""
Основы Python (2 урок, 4 задание)
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. И т.д...
"""
list_dann = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ',
             'директор аэлита']


@profile
def hello_name(lst):
    for i in list_dann:
        stroka = i.split(' ')
        names = stroka[-1]
        print(f' Привет, {names.title()}')


print(getsizeof(hello_name(list_dann)))


@profile
def hello_name_1(lst):
    list_1 = tuple(lst)
    return (f'Привет, {i.split(" ")[-1].title()}\n' for i in list_1)


print(*hello_name_1(list_dann), getsizeof(hello_name_1(list_dann)))

# В оптимизированом варианте я в функции list преобразую в tuple и в генераторе (вместо обычного цикла)
# беру нужные мне элементы.