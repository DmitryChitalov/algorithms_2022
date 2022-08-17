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


class StackofPlates:
    """Общий родительский класс для всех стопок с тарелками"""
    name: str = None

    def __init__(self, name: str, number):
        self.stack = []
        self.max_stack = 10
        self.list_of_plates = []
        self.name = name
        self.number = number

    def __str__(self):
        return f"Stack_{self.number}"
    __repr__ = __str__

    def push_in(self, plate):
        self.stack.append(plate)

    def pop_out(self):
        return self.stack.pop()

    def stack_size(self):
        return len(self.stack)


list_of_stacks = []


def adding_plates(number):
    plate_stack = list_of_stacks[-1]
    now_stack_num = int(plate_stack.__str__()[-1])
    size = plate_stack.stack_size()
    max_stack = plate_stack.max_stack
    while (size + 1) < max_stack:
        plate_stack.push_in(1)
        number -= 1
        size += 1
        if number == 0:
            return f'Тарелки уместились в стопке {list_of_stacks[-1]}'
    next_stack = StackofPlates('stack', now_stack_num+1)
    list_of_stacks.append(next_stack)
    adding_plates(number)


stack_1 = StackofPlates('stack', 1)  # Первую стопку создаем вручную
list_of_stacks.append(stack_1)  # Первую стопку вручную добавляем в список всех стопок с тарелками
num_of_plates = 8
print(f'Добавим {num_of_plates} тарелок')
adding_plates(num_of_plates)
print(f'Сейчас на столе {len(list_of_stacks)} стопка(-ок) тарелок: {list_of_stacks}')
print(f'В последней стопке {list_of_stacks[-1]}: {list_of_stacks[-1].stack_size()} тарелок')
print()
num_of_plates = 25
print(f'Добавим {num_of_plates} тарелок')
adding_plates(num_of_plates)
print(f'Сейчас на столе {len(list_of_stacks)} стопка(-ок) тарелок: {list_of_stacks}')
print(f'В последней стопке {list_of_stacks[-1]}: {list_of_stacks[-1].stack_size()} тарелок')
print()
