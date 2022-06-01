"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""

import random
from array import array
from unittest import result


class Stack:
    def __init__(self, max_size=4):
        self.__stacksize = max_size
        self.__data = list()

    def push(self, item):
        if self.size() < self.__stacksize:
            self.__data.append(item)
            return True
        return False

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None

    def top(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) -1]
        return None

    def is_emmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def clear(self):
        self.__data = []

    def __repr__(self):
        array = [str(val) for val in self.__data]
        array.reverse()
        return  '\n'.join(array)

number_list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

count = 5
result = []
for i in range(count):
    lst_val = [i for i in random.sample(number_list, k=5)]
    s = Stack(3)
    j = 0
    while s.push(lst_val[j]):
        j += 1
    result.append(s)
print(result)