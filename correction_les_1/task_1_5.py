"""
Комментарии после проверки:
1.
max
это встроенные имена
нарушение пеп-8
2.

(len(self.elems) - 1) * self.max + len(self.elems[len(self.elems) - 1])
внешние скобки не нужны
"""

# max переименовала
class StackPlates:
    def __init__(self, max_plates):
        self.elems = [[]]
        self.max_plates = max_plates  # максимальный размер стопки

    def __str__(self):
        return str(self.elems)

    def add_plate(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_plates:
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
        if len(self.elems[len(self.elems) - 1]) == 0:
            return 0
        return len(self.elems)

    """
    Скобки из комментария не внешние, а алгебраические, 
    но для наглядности переставила местами, чтобы глаза не мозолили, исходный вариант под #
    """
    def count_plates(self):
        return self.max_plates * (len(self.elems) - 1) + len(self.elems[len(self.elems) - 1])
        # return (len(self.elems) - 1) * self.max_plates + len(self.elems[len(self.elems) - 1])

    def del_stack(self):
        if len(self.elems) == 1:
            self.elems = [[]]
            return self.elems
        return self.elems.pop()


plates = StackPlates(3)  # поставили потолок 3
plates.add_plate(1)  # закидываем 5 тарелок
plates.add_plate(2)
plates.add_plate(3)
plates.add_plate(4)
plates.add_plate(5)
print(plates)  # посмотрим на две стопки
print(plates.del_plate())  # посмотрим на удалённую тарелку
print(plates)  # посмотрим на две стопки после удаления
print(plates.count_stack())  # посчитаем стопки
print(plates.count_plates())  # посчитаем тарелки
print(plates.del_stack())  # удалим последнюю стопку и посмотрим на неё
print(plates)  # посмотрим на одну стопку
plates.del_stack()  # удалим единственную стопку
print(plates)  # посмотрим на пустой список
plates.add_plate(1)  # добавим тарелку
print(plates)  # одна стопка с одной тарелкой
plates.del_plate()  # удалим одну тарелку
print(plates)  # смотрим пустой список
print(plates.count_plates())  # посчитаем тарелки
print(plates.count_stack())  # посчитаем стопки
