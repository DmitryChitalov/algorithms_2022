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


# немного отличный вариант от разбора
class MyStack:
    def __init__(self, limit):
        self.limit = limit
        self.els = [[]]

    def push_in(self, el):
        if len(self.els[len(self.els)-1]) < self.limit:
            self.els[len(self.els)-1].append(el)
        else:
            self.els.append([])
            self.els[len(self.els)-1].append(el)

    def pop_out(self):
        result = self.els[len(self.els)-1].pop()
        if len(self.els[len(self.els)-1]) == 0:
            self.els.pop()
        return result

    def stack_size(self):
        els_count = 0
        for stack in self.els:
            els_count += len(stack)
        return els_count


if __name__ == '__main__':
    new_stack = MyStack(10)
    i = 1
    while i <= 25:
        new_stack.push_in(i)
        i += 1
    print(new_stack.els)
    print(new_stack.pop_out())
    print(new_stack.stack_size())
