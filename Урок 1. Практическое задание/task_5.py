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
    def __init__(self):  # Создаём класс "Стопки" из массива стопок
        self.elems = [[]]

    def is_empty(self):  # Проведение проверки на наличие в "Стопках" элементов
        return self.elems == [[]]

    def push_in(self, el):  # Добавляем элемент в "Стопки". При переполнении очередной "министопки" создаём новую.
        if len(self.elems[-1]) < 3:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def show_all(self):  # Просматриваем содержимое "Стопок"
        return self.elems

    def pop_out(self):  # Убираем элемент с вершины последней "министопки" и возвращаем его значение
        if len(self.elems[-1]) > 0:
            return self.elems[-1].pop()
        else:
            del self.elems[-1]
            return self.elems[-1].pop()

    def get_val(self):  # Узнаём значение первого элемента с вершины последней "министопки"
        if len(self.elems[-1]) > 0:
            return self.elems[-1][-1]
        else:
            return self.elems[-2][-1]

    def stack_size(self):  # Узнаём общее количество элементов в "Стопках"
        return (len(self.elems) - 1) * 3 + len(self.elems[-1])


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(8)
    SC_OBJ.push_in(9)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in(11)

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # узнаем размер стека
    print(SC_OBJ.stack_size())

    # смотрим, какие элементы имеются в стеке
    print(SC_OBJ.show_all())
    # убираем и возвращаем последний элемент в стеке
    print(SC_OBJ.pop_out())
    # смотрим, какие элементы стались в стеке
    print(SC_OBJ.show_all())

    # проверяем работу стека по удалению последних элементов
    print(SC_OBJ.pop_out())
    print(SC_OBJ.show_all())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.show_all())

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())
