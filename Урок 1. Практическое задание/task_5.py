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
        self.elems = []
        self.stackpack = []

    def is_empty(self):
        if not self.stackpack:
            return self.elems == []
        else:
            return

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) == 5:
            print(
                f"Превышен предельный размер стопки (5 элементов). Cоздана новая ({len(self.stackpack) + 2}) стопка "
                f"для заполнения.")
            self.stackpack.append(self.elems)
            self.elems = []
            self.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.stackpack) * 5 + len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> проверим стек на пустоту

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.4)
    SC_OBJ.push_in(12.4)
    SC_OBJ.push_in(5.8)
    SC_OBJ.push_in(7.5)
    SC_OBJ.push_in('False1')
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(22)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in('False1')
    SC_OBJ.push_in(2)

    print(SC_OBJ.get_val())  # -> получаем значение первого элемента с вершины стека без его удаления

    print(SC_OBJ.stack_size())  # -> узнаем размер стека со всеми стопками

    print(SC_OBJ.is_empty())  # -> проверяем последнюю/текущую стопку на пустоту

    SC_OBJ.push_in(4)  # -> добавляем еще один элемент в стек

    # удаляем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())

    # выводим заполненные стопки и стопку в процессе заполнения
    print(f" Собранные стопки: {SC_OBJ.stackpack}, стопка в процессе сбора: {SC_OBJ.elems}")
