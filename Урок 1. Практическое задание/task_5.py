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


class StackOfPlates:

    def __init__(self):
        self.plates = [[]]
        self.__max_plates = 4

    def is_empty(self):
        """Проверка на пустоту"""
        return self.plates == [[]]

    def push_in(self, el):
        """Добавить значение"""
        if len(self.plates[-1]) > self.__max_plates:
            new_plates = [el]
            self.plates.append(new_plates)
        else:
            self.plates[-1].append(el)

    def pop_out(self):
        """Взять последнее значение"""
        if self.plates[-1]:
            return self.plates[-1].pop()
        elif self.is_empty():
            print('Stack is empty!')
        else:
            self.plates.remove([])
            return self.plates[-1].pop()

    def get_val(self):
        """Получить последнее значение"""
        if self.plates[-1]:
            return self.plates[-1][len(self.plates[-1]) - 1]
        elif self.is_empty():
            print('Stack is empty!')
        else:
            self.plates.remove([])
            return self.plates[-1][len(self.plates[-1]) - 1]

    def stack_size(self):
        """Колличество стопок"""
        return len(self.plates)

    def plates_size(self):
        """Количество тарелок в последней стопке"""
        return len(self.plates[-1])


if __name__ == '__main__':

    stack_of_plates = StackOfPlates()
    print(stack_of_plates.is_empty())

    for i in range(1, 10 + 1):
        stack_of_plates.push_in(i)

    print(stack_of_plates.stack_size())
    stack_of_plates.pop_out()
    stack_of_plates.pop_out()
    stack_of_plates.pop_out()
    stack_of_plates.pop_out()
    stack_of_plates.pop_out()
    stack_of_plates.pop_out()
    print(stack_of_plates.plates)
    print(stack_of_plates.get_val())
    print(stack_of_plates.is_empty())
    print(stack_of_plates.plates_size())
    # Доработок не требуется
