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
from time import perf_counter


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = perf_counter()
        res = func(*args, **kwargs)
        stop = perf_counter()
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        print(f'Функция {func.__name__}, выполнение заняло: {mem_dif} Mib, время выполнения: {stop - start}')
        return res

    return wrapper


"""
Попробую оптимизировать из того же пеового ДЗ свою конструкцию для работы со стеком
StackMultyClass - оригинальная конструкция
"""


class StackMultyClass:
    def __init__(self, substack_size):
        self.elems = []
        self.size = substack_size

    def is_empty(self):
        return self.elems == []

    def show_stack(self):
        print(f'Substack size: {self.size}\n', self.elems)

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        for i in range(len(self.elems)):
            if len(self.elems[len(self.elems) - 1 - i]) == self.size:
                self.elems.append([])
                self.elems[len(self.elems) - 1 - i].append(el)
                break
            else:
                self.elems[len(self.elems) - 1 - i].append(el)
                break

    def pop_out(self):
        for i in range(len(self.elems)):
            temp_val = self.elems[len(self.elems) - 1 - i].pop()
            if len(self.elems[len(self.elems) - 1 - i]) == 0:
                self.elems.pop()
            return temp_val


class StackMultyClassSecond:
    __slots__ = ['elems', 'size']

    def __init__(self, substack_size):
        self.elems = []
        self.size = substack_size

    def is_empty(self):
        return self.elems == []

    def show_stack(self):
        print(f'Substack size: {self.size}\n', self.elems)

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        for i in range(len(self.elems)):
            if len(self.elems[len(self.elems) - 1 - i]) == self.size:
                self.elems.append([])
                self.elems[len(self.elems) - 1 - i].append(el)
                break
            else:
                self.elems[len(self.elems) - 1 - i].append(el)
                break

    def pop_out(self):
        for i in range(len(self.elems)):
            temp_val = self.elems[len(self.elems) - 1 - i].pop()
            if len(self.elems[len(self.elems) - 1 - i]) == 0:
                self.elems.pop()
            return temp_val


@memory
def measure_func_1(substack_num=50, el_num=1000000):
    """
    Функция-сценарий для создания элемента класса, наполнения его даннымии, и опустошение.
    substack_num - количество "стопок"
    el_num=1000000 - количество элементов, которых мы заносим  в объект класса
    Замеряю работу данных функций
    """
    object_1 = StackMultyClass(substack_num)
    # заполняем:
    for el in range(el_num):
        object_1.push_in(el)
    # опустошаем:
    for el in range(el_num):
        object_1.pop_out()


@memory
def measure_func_2(substack_num=50, el_num=1000000):
    """
    Функция-сценарий для создания элемента класса, наполнения его даннымии, и опустошение.
    substack_num - количество "стопок"
    el_num=1000000 - количество элементов, которых мы заносим  в объект класса
    Замеряю работу данных функций
    """
    object_1 = StackMultyClassSecond(substack_num)
    # заполняем:
    for el in range(el_num):
        object_1.push_in(el)
    # опустошаем:
    for el in range(el_num):
        object_1.pop_out()


measure_func_1()
measure_func_2()

"""
Итак, мои результаты измерений:
Функция measure_func_1, выполнение заняло: 1.109375 Mib, время выполнения: 1.166570800007321
Функция measure_func_2, выполнение заняло: 1.00390625 Mib, время выполнения: 1.056273499969393
Может быть цифры оптимизации и не так впечатляют, но, на мой взгляд это однозначно очень крутое решение.
Всего одной! строчкой кода мы добились и снижения использования памяти, и увеличения скорости исполнения!
Конечно, это очень наглядно сработало в примере, где исполльзуются "быстрые" операции над списком - добавление элемента 
в конец, и удаление элемента с конца списка.
"""
