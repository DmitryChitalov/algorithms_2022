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

class PlatesStacks:
    def __init__(self):
        self.elems = [[]]

    def __get__(self):
        print(self.elems)

    @classmethod
    def not_full_stack(cls, size): #метод класса проверяет, полная ли последняя стопка
        if size < 3:
            return True
        else:
            return False

    def is_empty(self):
        return self.elems == [[]]

    def get_stack_number(self): # возвращает количество стопок
        return len(self.elems)

    def add(self, item): # добавляет тарелки в последнюю неполную или следующую свободную стопку
        if self.not_full_stack(len(self.elems[len(self.elems)-1])):
            self.elems[len(self.elems)-1].insert(0, item)
        else:
            self.elems.append([item])

    def from_stack(self):
        return self.elems[len(self.elems)-1].pop()

    def size(self):    # возвращает размер стопок
        size_stacks = []
        for i in range(len(self.elems)):
            size_stacks.append(len(self.elems[i]))
        return size_stacks




if __name__ == '__main__':
    plates_obj = PlatesStacks()
    plates_obj.add('plate')
    plates_obj.add('plate')
    plates_obj.add('plate')
    plates_obj.add('plate')
    plates_obj.add('plate')
    print(plates_obj.is_empty())
    plates_obj.__get__()
    print(plates_obj.get_stack_number())
    print(plates_obj.size())
    plates_obj.from_stack()
    plates_obj.__get__()
    print(plates_obj.size())
