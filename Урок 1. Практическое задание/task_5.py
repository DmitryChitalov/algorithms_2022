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
class Stack_Plates:
    def __init__(self):
        self.plates = []

    def is_empty(self):
        return self.plates == []

    def push_in(self, plate):
        self.plates.append(plate)

    def pop_out(self):
        return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        return len(self.plates)


def plates_stack(count_of_plates):
    stack_obj = Stack_Plates()

    for plate in range(1, count_of_plates + 1):
        stack_obj.push_in(plate)
        if stack_obj.stack_size() == 10:
            print(stack_obj.plates)
            stack_obj = Stack_Plates()
    if stack_obj.is_empty():
        return
    print(stack_obj.plates)


plates_stack(99)
