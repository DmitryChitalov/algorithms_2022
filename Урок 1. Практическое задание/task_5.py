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
    def __init__(self):
        self.elements = [[], [], [], [], [], []]


    def push_in(self, member):
        """Верхний элемент стека находится в конце списка"""
        for index in range(0, len(self.elements), 1):
            if len(self.elements[index]) < 10:
                self.elements[index].append(member)
                break

    def pop_out(self):
        return self.elements.pop()

    def get_val(self):
        return self.elements[len(self.elements) - 1]

    def stack_size(self):
        return len(self.elements)


if __name__ == '__main__':
    new_stack_number_one = StackClass()
    number_of_stack_members = 0
    while number_of_stack_members < 55:
        new_stack_number_one.push_in(1+number_of_stack_members)
        number_of_stack_members += 1

    print(new_stack_number_one.elements)

print(new_stack_number_one.get_val())
print(new_stack_number_one.stack_size())
print(new_stack_number_one.pop_out())
print(new_stack_number_one.stack_size())
print(new_stack_number_one.stack_size())
print(new_stack_number_one.pop_out())
print(new_stack_number_one.stack_size())

