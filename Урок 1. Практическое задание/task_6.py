"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # x.insert(0, 3)
        self.stack.insert(0, item)

    def pop(self):
        removed = self.stack.pop()
        return removed

    def stack_size(self):
        return len(self.stack)

    def stack_remove(self, element, item):
        element.stack.insert(0, item.pop())

    def show_elements(self):
        return (self.stack)




if __name__ == '__main__':
    stack_base = Stack()
    stack_remake = Stack()
    stack_ready = Stack()

    print(stack_base.stack_size())
    print(stack_remake.stack_size())
    print(stack_ready.stack_size())
    stack_base.push('1')
    stack_base.push('2')
    stack_base.push('22')
    print(stack_base.stack_size())

    stack_base.stack_remove(stack_remake, stack_base)

    print(stack_base.stack_size())
    print(stack_remake.stack_size())
    print(stack_ready.stack_size())
    print(stack_remake.show_elements())
