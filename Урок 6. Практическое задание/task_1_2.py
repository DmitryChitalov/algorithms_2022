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
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Исходное решение - задание 3_3 из курса 'Основы языка Python'
@decor
def thesaurus(names):
    dict_of_names = {}
    for name in names:
        a = name[0]
        list_of_names = list(filter(lambda el: el.startswith(a), names))
        dict_of_names.setdefault(a, list_of_names)
    return dict_of_names


# Оптимизированное решение
@decor
def thesaurus2(names):
    dict_of_names2 = {name[0]: list(filter(lambda el: el.startswith(name[0]), names)) for name in names}
    return dict_of_names2


if __name__ == '__main__':
    your_names = input('Введите имена сотрудников через запятую: ')  # иван, борис, петр, ирина, алексей, михаил
    names = sorted(your_names.split(', '))
    print('Исходное решение')
    res1, mem_dif = thesaurus(names)
    print(res1)
    print(f'Выполнение исходного решения заняло {mem_dif} Mib')  # 0.0078125 Mib
    print('\nОптимизированное решение')
    res2, mem_dif = thesaurus2(names)
    print(res2)
    print(f'Выполнение оптимизированного решения заняло {mem_dif} Mib')  # 0.00390625 Mib
