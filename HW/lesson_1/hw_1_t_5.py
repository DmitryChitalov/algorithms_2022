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

class StackPlates:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def is_empty(self):
        return self.elems==[[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems)-1]) < self.max_size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]


if __name__ == '__main__':


    SP_OBJ = StackPlates(5)

    print(SP_OBJ.is_empty())
    SP_OBJ.push_in()
    SP_OBJ.push_in(1)
    SP_OBJ.push_in(5)
    SP_OBJ.push_in(1)
    SP_OBJ.push_in(5)
    SP_OBJ.push_in(1)
    SP_OBJ.push_in(5)
    SP_OBJ.push_in(1)
    SP_OBJ.push_in(5)
    SP_OBJ.pop_out()
    SP_OBJ.pop_out()
    SP_OBJ.pop_out()
    print(SP_OBJ.elems)


