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
        self.elems = [[]]
        self.st_size = 5
        self.st_num = 0
        self.count = 0

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if self.count >= self.st_size:
            self.elems.append([])
            self.count = 0
            self.st_num += 1
        self.elems[self.st_num].append(el)
        self.count += 1
        print('стек', self.elems)

    def pop_out(self):
        print('стек', self.elems)
        self.count -= 1
        if self.count < 0:
            self.count = self.st_size -1
            self.elems.remove([])
            if self.st_num > 0:
                self.st_num -= 1
            else:
                print('End of Stack')
                raise SystemExit

        return self.elems[self.st_num].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in(22)
    SC_OBJ.push_in(17)
    SC_OBJ.push_in(27)
    SC_OBJ.push_in(44)
    SC_OBJ.push_in(19)
    SC_OBJ.push_in(11)
    SC_OBJ.push_in(21)
    SC_OBJ.push_in(12)
    SC_OBJ.push_in(77)
    SC_OBJ.push_in(99)
    SC_OBJ.push_in(18)
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    SC_OBJ.push_in(16)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in(22)
    SC_OBJ.push_in(17)
    SC_OBJ.push_in(27)
    SC_OBJ.push_in(44)

    # print(SC_OBJ)