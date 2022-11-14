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

class StackOfPlates(object):
    """ Класс 'Стопка тарелок'. 

    Args:
        stack_limit (int): максимальный размер стопки
    
    Methods:
        is_empty    -> bool : Проверка стека на наличие элементов.
        put_plate   -> None : Создать новый стек при переполнении предыдущего или пустом стеке стеков и добавить в него элемент.
        take_plate  -> None : Вернуть последний элемент из стека.
        show_stacks -> str  : Показать количество элементов стопок с количество стопок.
    """

    __slots__ = ('stack_of_stacks', 'stack_limit')

    def __init__(self, stack_limit: int) -> None:
        self.stack_of_stacks: list = []
        self.stack_limit: int = stack_limit

    def is_empty(self) -> bool:
        # Проверить стек на наличие элементов.
        return self.stack_of_stacks == []

    def put_plate(self) -> None:
        # Создать новый стек при переполнении предыдущего или пустом стеке стеков и добавить в него элемент
        if self.is_empty() or len(self.stack_of_stacks[-1]) == self.stack_limit:
            self.stack_of_stacks.append([])
        self.stack_of_stacks[-1].append('plate')
    
    def take_plate(self) -> None:
        # Вернуть последний элемент из стека
        if self.is_empty():
            print("No plate to take.")
        elif not self.is_empty() and len(self.stack_of_stacks[-1]) == 1:
            self.stack_of_stacks[-1].pop()
            self.stack_of_stacks.pop()
        else:
            self.stack_of_stacks[-1].pop()

    def show_stacks(self) -> str:
        # Показать количество элементов стопок с количество стопок.
        if self.is_empty():
            print("Stack is empty.")
        else:
            for number, stack in enumerate(self.stack_of_stacks):
                print(f'Stack number {number + 1}:  {stack}')

    def __str__(self) -> str:
        if self.is_empty():
            return 'Stack is empty'
        else:
            sum_of_plates: int = sum([len(stack) for stack in self.stack_of_stacks])
            len_stack_of_stacks: int = len(self.stack_of_stacks)
            return f"{sum_of_plates} plats in {len_stack_of_stacks} staks."


if __name__ == '__main__':
    
    stacks = StackOfPlates(stack_limit=4)
    for _ in range(9):
        stacks.put_plate()
    stacks.show_stacks()
    print(stacks)

    for _ in range(5):
        stacks.take_plate()
    stacks.show_stacks()
    print(stacks)

    for _ in range(5):
        stacks.take_plate()
    stacks.show_stacks()
    print(stacks)
    
    