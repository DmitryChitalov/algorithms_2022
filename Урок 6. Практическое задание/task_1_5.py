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
'''Курс основы урок 10 задание 1
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.'''
from random import randint
from memory_profiler import memory_usage
from collections import deque


def decor(func):
    def wrapper(*arg):
        m1 = memory_usage() # текущее использование памяти
        func(*arg)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'dif {mem_diff} m1 {m1} m2 {m2}')
        # return  mem_diff
    return wrapper


class Matrix():

    def __init__(self, x, y, num_py):
        self.main_li = self.array_generator(x, y, num_py)

    def array_generator(self, x, y, num_py=False):
        if num_py:
            owner_li = deque()
        else:
            owner_li = []
        for _ in range(x):
            if num_py:
                inner_li = deque()
            else:
                inner_li = []
            for _ in range(y):
                inner_li.append(randint(1,1000))
            owner_li.append(inner_li)
        return owner_li

    def __str__(self):
        res = ''
        for i in self.main_li:
            res += '\n'
            for j in i:
                res += f"{j} "
        return res


    def __add__(self, new):
        new_matrix = []
        for num_i, i in enumerate(self.main_li):
            inner_li = []
            for num_j, j in enumerate(i):
                inner_li.append(j+new.main_li[num_i][num_j])
            new_matrix.append(inner_li)

        return Matrix(new_matrix)



col = 1000
row = 8000

@decor
def test_func1():
    mx = Matrix(col, row, False)  # Тестирование до оптимизации
    del mx

@decor
def test_func2():
    mx = Matrix(col, row, True)  # Тестирование после оптимизации
    del mx

# memory_usage(test_func2)    # 65.65234375
memory_usage(test_func1)  # 42.3046875

'''При использовании deque вместо list для матриц размером 1000 на 8000 разница в экономии 
памяти составила 23.34765625'''




