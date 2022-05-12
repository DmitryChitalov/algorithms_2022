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
    def __init__(self, max_size):
        self.stacks = []
        self.st_count = -1
        if max_size >= 1:
            self.max_size = max_size
        else:
            raise ValueError("Минимальный размер стопки : 1 тарелка")

    def is_empty(self):
        return self.stacks == []

    def push_in(self, el):
        if self.st_count == -1:
            self.stacks.append([])
            self.st_count = 0
        if len(self.stacks[self.st_count]) < self.max_size:
            self.stacks[self.st_count].append(el)
        else:
            self.st_count += 1
            self.stacks.append([])
            self.stacks[self.st_count].append(el)

    def pop_out(self):
        if len(self.stacks[self.st_count]) > 1:
            return self.stacks[self.st_count].pop()
        else:
            res = self.stacks[self.st_count].pop()
            self.stacks.pop()
            self.st_count -= 1
            return res

    def print_out(self):
        res = ""
        for el in self.stacks:
            res = f'{res}\n{el}'
        return res.strip()

    def stack_size(self):
        res = 0
        for st in self.stacks:
            res += len(st)
        return res

    def stack_count(self):
        return self.st_count+1

    def get_val(self):
        if not(self.is_empty()):
            return self.stacks[self.st_count][-1]


if __name__ == "__main__":
    my_stack = StackClass(4)
    print("Заполняем стопки 13ю тарелками, по 4 тарелки в стопке")
    for i in range(13):
        my_stack.push_in(i+1)
    print(my_stack.print_out())
    print("Количество стопок:", my_stack.stack_count())
    print("Количество тарелок:", my_stack.stack_size())
    print("Убираем 5 тарелок:")
    for i in range(5):
        print(my_stack.pop_out(), end="  ")
    print()
    print("Оставшиеся:")
    print(my_stack.print_out())
    print("Количество стопок:", my_stack.stack_count())
    print("Количество тарелок:", my_stack.stack_size())
    my_stack.push_in(14)
    print("Добавляем еще 1 тарелку:")
    print(my_stack.print_out())
    print("Количество стопок:", my_stack.stack_count())
    print("Количество тарелок:", my_stack.stack_size())
    print("Проверяем пустой стек или нет:", my_stack.is_empty())
    print("Следующей будет убрана тарелка:", my_stack.get_val())
    print("Убираем еще 9 тарелок")
    for i in range(9):
        print(my_stack.pop_out(), end="  ")
    print()
    print("Количество стопок:", my_stack.stack_count())
    print("Количество тарелок:", my_stack.stack_size())
    print("Проверяем пустой стек или нет:", my_stack.is_empty())
