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
        self.elem = []

    def is_empty(self):
        return self.elem == []

    def to_q(self, item):
        self.elem.insert(0, item)

    def from_queue(self):
        return self.elem.pop()

    def size(self):
        return len(self.elem)


class BoardTasks:
    def __init__(self):
        self.base_q = QueueClass()
        self.rev_q = QueueClass()
        self.solved_task = []

    def task_solving(self):
        task = self.base_q.from_queue()
        self.solved_task.append(task)

    def task_revision(self):
        task = self.base_q.from_queue()
        self.rev_q.to_q(task)

    def task_add(self, task):
        self.base_q.to_q(task)


if __name__ == '__main__':

    desk1 = BoardTasks()

    print(desk1.base_q.elem)
    desk1.task_add('Task1')
    desk1.task_add('Task2')
    desk1.task_add('Task3')
    print(desk1.base_q.elem)

    desk1.task_solving()
    desk1.task_revision()
    print(desk1.base_q.elem)
    print(desk1.rev_q.elem)
    print(desk1.solved_task)