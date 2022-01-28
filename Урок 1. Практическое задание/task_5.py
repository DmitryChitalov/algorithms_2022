"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""
class StackClass:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_elems = []
        self.elems =[]
        self.stack_elems.append(self.elems)
        self.count_elems = 0

    def is_empty(self):
        return self.elems == [] # выводит True если стек не пустой

    def push_in(self, el):     # заполняем стек
        self.count_elems += 1   # при каждом вызове функции плюсуем общий счетчик
        if len(self.elems) < self.max_size:   # добавляем элементы пока размер стопки меньше указанной
            self.elems.append(el)
        else:
            self.elems = []
            self.elems.append(el)
            self.stack_elems.append(self.elems)

    def pop_out(self):

        if self.count_elems == 0:
            return f"В стеке нет элементов"
        else:
            self.count_elems -= 1
            result = self.stack_elems[len(self.stack_elems) - 1].pop()  # тут подсмотрел ставил просто индекс -1,недодумал.
            if len(self.stack_elems[len(self.stack_elems) - 1]) == 0:
                self.stack_elems.pop()

            return result  # удаляем и выводим последний элемент стека

    def stack_size(self):
        return f"В стеке -- {len(self.stack_elems)} стоп(-ки,-ка,-ок), размер стопки -- {self.max_size}," \
               f" всего -- {self.count_elems} элемент(-ов,-а)" # выводим размер стека




if __name__ == '__main__':
    SC_OBJ = StackClass(2)

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    print(SC_OBJ.is_empty())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.stack_elems)
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())


