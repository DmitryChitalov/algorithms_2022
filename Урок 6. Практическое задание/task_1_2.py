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
from memory_profiler import profile
from timeit import timeit


class PlateClass1:
    def __init__(self):
        self.lst = [[]]
        self._max = 3  # максимум в стопке
        self._current = 0  # Текущая стопка

    def is_empty(self):
        return self.lst == [[]]

    def push_in(self, el):
        if len(self.lst[self._current]) >= self._max:
            self._current += 1
            self.lst.append([])
        self.lst[self._current].append(el)

    def pop_out(self):
        par = self.lst[self._current].pop()
        if len(self.lst[self._current]) == 0:
            if self._current == 0:
                raise NameError('Ошибка ввода данных!')
            self._current -= 1
            self.lst.pop()

    def __str__(self):

        return (f'{self.lst}')

    def stack_size(self):
        return (self._current + 1)


class PlateClass2:
    __slots__ = ('lst', '_max', '_current')

    def __init__(self):
        self.lst = [[]]
        self._max = 3  # максимум в стопке
        self._current = 0  # Текущая стопка

    def is_empty(self):
        return self.lst == [[]]

    def push_in(self, el):
        if len(self.lst[self._current]) >= self._max:
            self._current += 1
            self.lst.append([])
        self.lst[self._current].append(el)

    def pop_out(self):
        par = self.lst[self._current].pop()
        if len(self.lst[self._current]) == 0:
            if self._current == 0:
                raise NameError('Ошибка ввода данных!')
            self._current -= 1
            self.lst.pop()

    def __str__(self):

        return (f'{self.lst}')

    def stack_size(self):
        return (self._current + 1)


@profile
def var1():
    Pl = PlateClass1()
    for j in range(70000):
        Pl.push_in(j)

    # print(Pl)
    print(f'количество стопок {Pl.stack_size()}')

    for j in range(3):
        Pl.pop_out()

    # print(Pl)
    print(f'количество стопок {Pl.stack_size()}')


@profile
def var2():
    Pl = PlateClass2()
    for j in range(70000):
        Pl.push_in(j)

    # print(Pl)
    print(f'количество стопок {Pl.stack_size()}')

    for j in range(3):
        Pl.pop_out()

    # print(Pl)
    print(f'количество стопок {Pl.stack_size()}')


var1()
var2()
'''
Использовал __slots__ в классе, выигрыш по памяти в 2 раза, быстродействие не изменилось.
'''
# print(timeit("var1()", globals=globals(), number=10))
# print(timeit("var2()", globals=globals(), number=10))
