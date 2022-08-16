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

class plates_stacks:

    max_stack_size = 5

    def __init__(self):
        self.lst = [[]]


    def plus_plates(self, plate):
         if len(self.lst[len(self.lst)-1]) < self.max_stack_size:
             self.lst[len(self.lst)-1].append(plate)
         else:
             self.lst.append([plate])

    def show_plates(self):
        print(self.lst)

    def minus_plate(self):
        if len(self.lst[len(self.lst) - 1]) == 1:
            return self.lst.pop()[0]
        else:
            return self.lst[len(self.lst) - 1].pop()


some_plates = plates_stacks()

some_plates.plus_plates('small_plate')
some_plates.plus_plates('big_plate')
some_plates.plus_plates('broken_plate')
some_plates.plus_plates('good_plate')
some_plates.plus_plates('dirty_plate')
some_plates.plus_plates('deep_plate')
some_plates.plus_plates('tall_plate')

some_plates.show_plates()

print(some_plates.minus_plate())

some_plates.show_plates()

print(some_plates.minus_plate())
print(some_plates.minus_plate())

some_plates.show_plates()




