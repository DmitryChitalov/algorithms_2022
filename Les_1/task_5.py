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

"""
Что нужно включить в класс:
    1. инициализация
    2. str - чтобы смотреть на тарелки
    2. функцию add, добавляющую тарелки сверху стопки не более max, в противном случае создаёт новую стопку
        проверяем длину списка на максимум, складываем тарелку, если меньше; иначе создаём новый список для тарелок
    3. функцию del, убирающую тарелки сверху
        удаляем тарелку из стопки, если тарелка последняя в стопке(списке), удаляем этот список
        возвращаем стопки без последней тарелки и отдельно выдаём удалённую тарелку
        проверка на последнюю тарелку в единственной стопке, нужна "пусткая" стопка, 
            иначе потом не получится в неё добавлять тарелки
    4. функцию count, считающую количество стопок
        проверка на пустую стопку, должен вернуться 0
    5. функцию count, считающую количество тарелок
    6. функцию del, удаляющую последнюю стопку
         если стопка одна, нужно превратить стопку в [[]], иначе потом не получится в неё добавлять элементы
"""


class StackPlates:
    def __init__(self, max):
        self.elems = [[]]
        self.max = max  # максимальный размер стопки

    def __str__(self):
        return str(self.elems)

    def add_plate(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def del_plate(self):
        if len(self.elems[len(self.elems) - 1]) == 1:
            self.elems = [[]]
            return self.elems
        new_stack = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return new_stack

    def count_stack(self):
        if len(self.elems[len(self.elems)-1]) == 0:
            return 0
        return len(self.elems)

    def count_plates(self):
        return (len(self.elems) - 1) * self.max + len(self.elems[len(self.elems) - 1])

    def del_stack(self):
        if len(self.elems) == 1:
            self.elems = [[]]
            return self.elems
        return self.elems.pop()


plates = StackPlates(3) # поставили потолок 3
plates.add_plate(1) # закидываем 5 тарелок
plates.add_plate(2)
plates.add_plate(3)
plates.add_plate(4)
plates.add_plate(5)
print(plates)  # посмотрим на две стопки
print(plates.del_plate())  # посмотрим на удалённую тарелку
print(plates)  # посмотрим на две стопки после удаления
print(plates.count_stack())  # посчитаем стопки
print(plates.count_plates())  # посчитаем тарелки
print(plates.del_stack()) # удалим последнюю стопку и посмотрим на неё
print(plates) # посмотрим на одну стопку
plates.del_stack() # удалим единственную стопку
print(plates) # посмотрим на пустой список
plates.add_plate(1) # добавим тарелку
print(plates) # одна стопка с одной тарелкой
plates.del_plate() # удалим одну тарелку
print(plates) # смотрим пустой список
print(plates.count_plates()) # посчитаем тарелки
print(plates.count_stack()) # посчитаем стопки
