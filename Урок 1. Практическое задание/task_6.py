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

class QueueTasks:
    def __init__(self):
        self.queue_tasks = []
        self.solved_tasks = []
        self.active_tasks = []
        self.revisions = []

    def is_empty_new_tasks(self):
        return self.queue_tasks == []

    def is_empty_in_process(self):
        return self.active_tasks == []

    def is_empty_solved(self):
        return self.solved_tasks == []

    def is_empty_revisions(self):
        return self.revisions == []

#  удалить последний элемент

    def pop_out_from_queue(self):
        self.queue_tasks.pop()

    def pop_out_from_active(self):
        self.active_tasks.pop()

    def pop_out_from_solved(self):
        self.solved_tasks.pop()

    def pop_out_from_revisions(self):
        self.revisions.pop()

#  добавить в очередь

    def new_task(self, task):
        self.queue_tasks.insert(0, task)

    def to_active_tasks_from_queue(self):
        self.active_tasks.insert(0, self.queue_tasks[-1])
        self.pop_out_from_queue()

    def to_queue_from_revisions(self):
        self.active_tasks.insert(0, self.revisions[-1])
        self.pop_out_from_revisions()

    def to_solved(self):
        self.solved_tasks.insert(0, self.active_tasks[-1])
        self.pop_out_from_active()

    def to_revisions(self):
        self.revisions.insert(0, self.solved_tasks[-1])
        self.pop_out_from_solved()


# общее число задач

    def total_tasks_number(self):
        return len(self.queue_tasks) + \
               len(self.active_tasks) + \
               len(self.solved_tasks) + len(self.revisions)

# показать всё

    def show_all(self):
        return {'Задачи в очереди:':  self.queue_tasks,
         'Задачи в работе:': self.active_tasks,
         'Завершённые задачи': self.solved_tasks,
         'На доработку': self.revisions}


if __name__ == '__main__':
    project = QueueTasks()
    [project.new_task(f'Задача {i}') for i in range(1, 11)]

    [print(*el) for el in project.show_all().items()]
    print(f'{"*" * 50}\nВсего задач: {project.total_tasks_number()}\n')

    for i in range(0, 7): project.to_active_tasks_from_queue()
    for i in range(0, 5): project.to_solved()
    for i in range(0, 2): project.to_revisions()

    [print(*el) for el in project.show_all().items()]
    print(f'{"*" * 50}\nВсего задач: {project.total_tasks_number()}')

