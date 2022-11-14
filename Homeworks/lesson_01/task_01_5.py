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


class StackPlatesClass:
    def __init__(self):
        self.plates_lst = []

    def is_empty(self):
        return self.plates_lst == []

    def view(self):
        print(self.plates_lst)

    def push_in(self):
        if len(self.plates_lst) == 0 or len(self.plates_lst[-1]) == 3:
            self.plates_lst.append([])
        number_plates = len(self.plates_lst[-1])
        self.plates_lst[-1].append(number_plates + 1)

    def del_out(self):
        if len(self.plates_lst) == 0:
            print('Тарелок больше нет.')
        else:
            number_stacks = len(self.plates_lst) - 1
            del self.plates_lst[number_stacks][-1]
            if len(self.plates_lst[number_stacks]) == 0:
                del self.plates_lst[-1]


if __name__ == '__main__':

    SPC_obj = StackPlatesClass()

    print(SPC_obj.is_empty())
    SPC_obj.view()

    for i in range(11):
        SPC_obj.push_in()
        SPC_obj.view()

    print(SPC_obj.is_empty())

    for i in range(12):
        SPC_obj.view()
        SPC_obj.del_out()

    print(SPC_obj.is_empty())
