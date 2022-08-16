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


class TaskBoard:
    def __init__(self):
        self.base_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.completed_tasks = []

    def closing_task(self):
        task = self.base_queue.from_queue()
        self.completed_tasks.append(task)

    def to_revision_task(self):
        task = self.base_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        self.base_queue.to_queue(item)

    def from_revision_task(self):
        task = self.revision_queue.from_queue()
        self.base_queue.to_queue(task)

    def current_task(self):
        return self.base_queue.elems[-1]

    def current_revision(self):
        return self.revision_queue.elems[-1]

    def count_base_queue(self):
        return self.base_queue.elems


if __name__ == '__main__':
    task = TaskBoard()
    task.to_current_queue('task1')
    task.to_current_queue('task2')
    task.to_current_queue('task3')
    task.to_current_queue('task4')
    print(task.current_task())
    task.to_revision_task()
    print(task.current_revision())
    print(task.count_base_queue())
