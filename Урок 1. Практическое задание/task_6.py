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

from random import random


class TaskBoard:
    def __init__(self):
        self.base = []
        self.queue = []
        self.solved = []

    def to_queue(self, item):
        r = round(random())
        if r == 0:
            self.queue.insert(0, item)
        else:
            self.solved.insert(0, item)

    def solve_queue(self):
        self.solved.extend(self.queue)
        self.queue.clear()

    def which_are_in_queue(self):
        return self.queue

    def which_are_solved(self):
        return self.solved

    def solved_lenght(self):
        return len(self.solved)

    def queue_lenght(self):
        return len(self.queue)


if __name__ == '__main__':
    brd = TaskBoard()

    brd.to_queue('mew')
    brd.to_queue(3)
    brd.to_queue(False)

    print(brd.which_are_in_queue())
    print(brd.which_are_solved())

    print(brd.queue_lenght())
    print(brd.solved_lenght())

    brd.solve_queue()

    print(brd.which_are_in_queue())
    print(brd.which_are_solved())

    print(brd.queue_lenght())
    print(brd.solved_lenght())
