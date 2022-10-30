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
# курс алгоритмы урок 4 задание 4
# Функция определяет число,
# которое встречается в массиве чаще всего
from memory_profiler import memory_usage
from random import randint


def memory_counter(func):
    def wrapper(*args):
        start = memory_usage()[0]
        result = func(*args)
        end = memory_usage()[0]
        memory_used = end - start
        print('Использовано памяти:', memory_used)
        return result
    return wrapper


@memory_counter
def function(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == '__main__':
    num_array = [randint(0, 100) for i in range(10000)]
    print(function(num_array))

    tpl = tuple(num_array)
    print(function(num_array))

# Использовано памяти: 0.03515625
# Чаще всего встречается число 28, оно появилось в массиве 132 раз(а)
# Использовано памяти: 0.00390625
# Чаще всего встречается число 28, оно появилось в массиве 132 раз(а)

# Список передаваемый функции заменён на кортеж, что значительно сократило потребление памяти во время работы функции
