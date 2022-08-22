"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackClass:
    def __init__(self):
        self.__elems = [[]]
        self.__indxi = 0
        self.__indxj = 0

    # Взять элемент из стопки
    def pop(self):
        if self.__indxi == 0 and self.__indxj == 0:
            print("Массив пуст. Удалять нечего")
            return
        self.__elems[self.__indxj].pop()
        self.__indxi -= 1

        if self.__indxi == 0:
            self.__elems.pop()
            if self.__indxi == 0 and self.__indxj == 0:
                return
            self.__indxi = 3
            self.__indxj -= 1

    # Добавить элемент в стопку
    def insert(self, elem):
        if self.__indxi > 3:
            self.__indxj += 1
            self.__elems.append([])
            self.__indxi = 0
        self.__elems[self.__indxj].append(elem)
        self.__indxi += 1

    # Печать всей стопки
    def print(self):
        print(self.__elems)


sss = StackClass()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.insert(3)
sss.insert(44)
sss.insert(3567)
sss.insert(3567)
sss.insert(3567)
sss.insert(3567)
sss.insert(3567)
sss.insert(3567)
sss.insert(3567)
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()
sss.pop()
sss.print()

