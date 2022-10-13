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

class StackOfPlates():
    def __init__(self):
        self.stacks = []
        self.plates_in_stack = 5  # Максимальное количество тарелок в стопке

    def stacks_is_empty(self):
        return not bool(self.stacks)

    def add_stack(self):
        self.stacks.append([])
    
    def remove_stack(self):
        self.stacks.pop()

    def add_plate(self):
        if self.stacks_is_empty() or len(self.stacks[-1]) == self.plates_in_stack:
            self.add_stack()
        self.stacks[-1].append('|')

    def remove_plate(self):
        if self.stacks_is_empty():
            print('Тарелок нет')
        elif len(self.stacks[-1]) == 0:
            self.remove_stack()
            if self.stacks_is_empty():
                print('Тарелок нет')
            else:
                self.stacks[-1].pop()
        else:
            self.stacks[-1].pop()

stack = StackOfPlates()

# Нет ни одной стопки с тарелками
print(stack.stacks)

# Добавляем 6 тарелок
stack.add_plate()
stack.add_plate()
stack.add_plate()
stack.add_plate()
stack.add_plate()
stack.add_plate()

print(stack.stacks)

# Удаляем 7 тарелок
stack.remove_plate()
stack.remove_plate()
stack.remove_plate()
stack.remove_plate()
stack.remove_plate()
stack.remove_plate()
stack.remove_plate()

print(stack.stacks)