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


class StackMultyClass:
    def __init__(self, substack_size):
        self.elems = []
        self.size = substack_size

    def is_empty(self):
        return self.elems == []

    def show_stack(self):
        print(f'Substack size: {self.size}\n', self.elems)

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        for i in range(len(self.elems)):
            if len(self.elems[len(self.elems) - 1 - i]) == self.size:
                self.elems.append([])
                self.elems[len(self.elems) - 1 - i].append(el)
                break
            else:
                self.elems[len(self.elems) - 1 - i].append(el)
                break

    def pop_out(self):
        for i in range(len(self.elems)):
            temp_val = self.elems[len(self.elems) - 1 - i].pop()
            if len(self.elems[len(self.elems) - 1 - i]) == 0:
                self.elems.pop()
            return temp_val



if __name__ == '__main__':

    SC_OBJ = StackMultyClass(2)   # <- можно и нужно менять количество элементов в "стопке"

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in('stop')
    SC_OBJ.push_in(True)
    SC_OBJ.push_in(4.7)
    SC_OBJ.push_in(0)
    # просматриваем результат
    SC_OBJ.show_stack()
    # удаляем элементы и просматриваем (получаеться лесенка в консоли)
    SC_OBJ.pop_out()
    SC_OBJ.show_stack()
    SC_OBJ.pop_out()
    SC_OBJ.show_stack()
    SC_OBJ.pop_out()
    SC_OBJ.show_stack()
    SC_OBJ.pop_out()
    SC_OBJ.show_stack()

