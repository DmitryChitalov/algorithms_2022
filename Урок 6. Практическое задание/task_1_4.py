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

Это файл для четвертого скрипта
"""
from memory_profiler import memory_usage
"""
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
"""


def memory_decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение функции {func.__name__} заняло {mem_diff} Mib')
        return res
    return wrapper


class PlatesStacks:
    """
    Стопка тарелок
    """
    @memory_decor
    def __init__(self, num):
        """ num - количество тарелок в одной стопке"""
        self.elems = []
        self.num = num
        self.param_1 = 1
        self.param_2 = 2
        self.param_3 = 3
        self.param_4 = 4
        self.param_5 = 5
        self.param_6 = 6
        self.param_7 = 7
        self.param_8 = 8
        self.param_9 = 9
        self.param_11 = 1
        self.param_12 = 2
        self.param_13 = 3
        self.param_14 = 4
        self.param_15 = 5
        self.param_16 = 6
        self.param_17 = 7
        self.param_18 = 8
        self.param_19 = 9

    def is_empty(self):
        """
        нет тарелок
        """
        return not self.elems

    def push_in(self, element):
        """ добавление тарелок """
        if not self.is_empty() and len(self.elems[len(self.elems) - 1]) < self.num:
            self.elems[-1].append(element)
        else:
            self.elems.append([element])

    def pop_out(self):
        """ удаление тарелок """
        return self.elems[-1].pop()

    def get_val(self):
        """ возвращение последней добавленной тарелки """
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        """ количество тарелок в сумме """
        if self.is_empty():
            return 0
        return (len(self.elems) - 1) * self.num + len(self.elems[-1])


class PlatesSlots:
    __slots__ = ['elems', 'num', 'param_1', 'param_2', 'param_3', 'param_4', 'param_5',
                 'param_6', 'param_7', 'param_8', 'param_9', 'param_11', 'param_12',
                 'param_13', 'param_14', 'param_15', 'param_16', 'param_17', 'param_18', 'param_19']

    @memory_decor
    def __init__(self, num):
        """ num - количество тарелок в одной стопке"""
        self.elems = []
        self.num = num
        self.param_1 = 1
        self.param_2 = 2
        self.param_3 = 3
        self.param_4 = 4
        self.param_5 = 5
        self.param_6 = 6
        self.param_7 = 7
        self.param_8 = 8
        self.param_9 = 9
        self.param_11 = 1
        self.param_12 = 2
        self.param_13 = 3
        self.param_14 = 4
        self.param_15 = 5
        self.param_16 = 6
        self.param_17 = 7
        self.param_18 = 8
        self.param_19 = 9


if __name__ == '__main__':
    ps_obj = PlatesStacks(4)
    plate = PlatesSlots(5)
""" 
Выполнение функции __init__ заняло 0.0078125 Mib
Выполнение функции __init__ заняло 0.0 Mib
Для оптимизации памяти мы применили слоты в ООП, 
что значительно уменьшает объем используемой памяти
"""
