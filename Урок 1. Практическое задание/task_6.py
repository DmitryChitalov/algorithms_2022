"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class MyQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_queue(self, item):
        self.elements.insert(0, item)

    def del_from_queue(self):
        if self.is_empty():
            return None
        return self.elements.pop()

    def size(self):
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.tasks_queue = MyQueue()
        self.revision_queue = MyQueue()
        self.log = []

    def resolve_task(self):
        self.log.append(self.tasks_queue.del_from_queue())

    def to_revision_task(self):
        task = self.tasks_queue.del_from_queue()
        if task:
            self.revision_queue.add_to_queue(task)

    def to_tasks_queue(self, item):
        self.tasks_queue.add_to_queue(item)

    def from_revision(self):
        task = self.revision_queue.del_from_queue()
        if task:
            self.tasks_queue.add_to_queue(task)

    def current_task(self):
        return self.tasks_queue.elements[len(self.tasks_queue.elements) - 1]


if __name__ == '__main__':
    work_tasks = TaskBoard()
    work_tasks.to_tasks_queue('task1')
    work_tasks.to_tasks_queue('task2')
    work_tasks.to_tasks_queue('task3')
    work_tasks.to_tasks_queue('task4')
    work_tasks.to_tasks_queue('task5')
    work_tasks.to_revision_task()
    work_tasks.resolve_task()
    print(f'Текущая задача: {work_tasks.current_task()}')
    print(f'Очередь задач: {work_tasks.tasks_queue.elements}')
    print(f'Задачи на доработку: {work_tasks.revision_queue.elements}')
    print(f'Выполненные задачи: {work_tasks.log}')
