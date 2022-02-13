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
    def __init__(self, max_count):
        self.current_elem = []
        self.stack_elem = []
        self.max_count = max_count

    def current_elem(self):
        return self.current_elem

    def stack_elem(self):
        return self.stack_elem

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.current_elem) == self.max_count-1:
            self.current_elem.append(el)
            self.stack_elem.append(self.current_elem)
            self.current_elem = []
        else:
            self.current_elem.append(el)

    def pop_out(self):
        if len(self.current_elem) != 0:
            return self.current_elem.pop()
        else:
            self.current_elem = self.stack_elem.pop()
            return self.current_elem.pop()

    def get_val(self):
        if len(self.current_elem) != 0:
            return self.current_elem[len(self.current_elem) - 1]
        else:
            return self.stack_elem[len(self.stack_elem)-1][len(self.stack_elem)]

    def size_full_stack(self):
        return len(self.stack_elem)

    def size_current_stack(self):
        return len(self.current_elem)


if __name__ == '__main__':

    SC_OBJ = StackPlatesClass(3)

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(599)
    SC_OBJ.push_in('oda')
    SC_OBJ.push_in('odvda')

    # проверяем содержание текущей стопки и всех ранее заполненных
    print(SC_OBJ.current_elem)
    print(SC_OBJ.stack_elem)

    # убираем 2 тарелки с вершины стека и возвращаем их значения
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())

    # проверяем содержание текущей стопки и всех ранее заполненных
    print(SC_OBJ.current_elem)
    print(SC_OBJ.stack_elem)

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # вновь узнаем размер стека
    print(SC_OBJ.size_full_stack())
    print(SC_OBJ.size_current_stack())

    # убираем 2 тарелки с вершины стека и возвращаем их значения
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())

    # проверяем содержание текущей стопки и всех ранее заполненных
    print(SC_OBJ.current_elem)
    print(SC_OBJ.stack_elem)

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())


