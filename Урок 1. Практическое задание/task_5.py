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
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)


    def __str__(self):
        return str(self.elems)

    def stack_size(self):
        return len(self.elems)


a = StackClass(5)
a.push_in(1)
a.push_in(1)
a.push_in(1)
a.push_in(1)
a.push_in(1)
a.push_in(1)
a.push_in(1)
print(a)
print()
print(a.stack_size())