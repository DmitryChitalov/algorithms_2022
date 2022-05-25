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
    def __init__(self):
        self.elems = []


    def push_in(self, el):
        if not self.elems:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) < 3:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)


    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return f'Stacks count: {len(self.elems)}'

if __name__ == '__main__':
    sp = StackPlates()
    sp.push_in('plate1')
    sp.push_in('plate2')
    sp.push_in('plate3')
    sp.push_in('plate4')
    sp.push_in('plate5')
    sp.push_in('plate6')
    print(sp.get_val())
    print(sp.pop_out())
    print(sp.get_val())
    print(sp.stack_size())