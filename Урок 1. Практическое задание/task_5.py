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


    def add_to_list(self, stackname):
        self.list_of_plates.append(stackname)

    def push_in(self, plate):
        self.stack.append(plate)

    def pop_out(self):
        return self.stack.pop()

    def stack_size(self):
        return len(self.stack)


def adding_plates(plate_stack, number):
    now_stack_num = int(plate_stack.__str__()[-1])
    while plate_stack.stack_size + number < plate_stack.max_stack:
        plate_stack.push_in(1)
        number -= 1
        if number == 0:
            break
    next_stack_num = StackofPlates('stack',now_stack_num+1)
    StackofPlates.add_to_list(next_stack_num)

stack_1 = StackofPlates('stack', 1)
adding_plates(stack_1, 15)


"""class Student:
    name: str = None

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Студент: " + self.name

    __repr__ = __str__


students = [Student(f"Студент_{i}") for i in range(20)]
print(students)"""
