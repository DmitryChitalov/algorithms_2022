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


class Plates_stack_Class:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Заполнение с созданием списков в списке с ограничением их длинны (стэк)"""
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        """удаление последнего элемента с последнего списка"""
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        """значение текучего элемента"""
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        """количество вложенных списков"""
        return len(self.elems)


if __name__ == '__main__':
    plates = Plates_stack_Class(2)

    plates.push_in('1')
    plates.push_in('2')
    plates.push_in('3')
    plates.push_in('4')
    plates.push_in('5')
    plates.push_in('6')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates)