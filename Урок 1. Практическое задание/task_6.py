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


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class BoardTasks:
    def __init__(self):
        self.base_queue = QueueClass()
        self.rev_queue = QueueClass()
        self.solved_tasks = []

    def task_solving(self):
        task = self.base_queue.from_queue()
        self.solved_tasks.append(task)

    def task_revision(self):
        task = self.base_queue.from_queue()
        self.rev_queue.to_queue(task)

    def task_add(self, task):
        self.base_queue.to_queue(task)


if __name__ == '__main__':

    desk1 = BoardTasks()

    print(desk1.base_queue.elems)
    desk1.task_add('Task1')
    desk1.task_add('Task2')
    desk1.task_add('Task3')
    print(desk1.base_queue.elems)

    desk1.task_solving()
    desk1.task_revision()
    print(desk1.base_queue.elems)
    print(desk1.rev_queue.elems)
    print(desk1.solved_tasks)












