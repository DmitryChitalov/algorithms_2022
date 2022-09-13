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
        self.items = []

    def is_empty(self):
        return self.items == []

    def to_queue(self, item):
        self.items.insert(0, item)

    def from_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class TaskType:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.alt_queue = QueueClass()
        self.solved_tasks = []  

    def resolved_task(self):
        task = self.cur_queue.from_queue()
        self.solved_tasks.append(task)

    def to_alteration_task(self):
        task = self.cur_queue.from_queue()
        self.alt_queue.to_queue(task)

    def to_current_queue(self, item):
        self.cur_queue.to_queue(item)

    def from_alteration(self):
        task = self.alt_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        return self.cur_queue.items[len(self.cur_queue.items) - 1]

    def current_revision(self):
        return self.alt_queue.items[len(self.alt_queue.items) - 1]


if __name__ == '__main__':
    task_type = TaskType()
    task_type.to_current_queue("Task1")
    task_type.to_current_queue("Task2")
    task_type.to_current_queue("Task3")
    task_type.to_current_queue("Task4")
    task_type.to_current_queue("Task5")
    print(task_type.cur_queue.items)
    print(task_type.current_task())
    task_type.to_alteration_task()
    task_type.resolved_task()
    task_type.from_alteration()
    print(task_type.cur_queue.items)
    print(task_type.current_task())
    print(task_type.solved_tasks)