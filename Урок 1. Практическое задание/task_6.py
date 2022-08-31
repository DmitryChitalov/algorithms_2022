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


class TaskBoard:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_to_base(self):
        self.base.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    task = TaskBoard()
    task.to_queue('Task1')
    task.to_queue('Task2')
    task.to_queue('Task3')
    print(task.base)
    (task.to_solved())
    print(task.solved)
    print(task.base)
    task.to_revision()
    print(task.revision)
    print(task.base)
    task.return_to_base()
    print(task.revision)
    print(task.base)
