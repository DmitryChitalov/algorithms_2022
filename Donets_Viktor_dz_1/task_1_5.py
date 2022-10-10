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
    def __init__(self, stack_quantity):
        self.elems = []
        self.st_qu = stack_quantity       # Количество тарелок в стопке
        self.init = 0

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
            self.elems[self.init].append(el)
        elif len(self.elems[self.init]) % self.st_qu == 0:
            self.elems.append([])
            self.init += 1
            self.elems[self.init].append(el)
        else:
            self.elems[self.init].append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass(10)

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')
    SC_OBJ.push_in('тарелка')

    # узнаем размер стека (колличество стопок)
    print(SC_OBJ.stack_size())  # -> 3

    print(SC_OBJ.is_empty())  # -> стек уже непустой

