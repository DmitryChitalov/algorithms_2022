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


class TaskQueueDesk:
    class TaskQueue:
        def __init__(self):
            self.tasks = []

        def __bool__(self):
            return bool(self.tasks)

        def new(self, task):
            self.tasks.append(task)

        def make(self):
            if self.tasks:
                return self.tasks.pop(0)

        def __str__(self):
            return self.tasks.__str__()

    def __init__(self):
        self.actual_tasks = self.TaskQueue()
        self.correst_tasks = self.TaskQueue()
        self.finish_tasks = []

    def new_task(self, task):
        self.actual_tasks.new(task)

    def to_edit(self):
        task=self.actual_tasks.make()
        if task:
            self.correst_tasks.new(task)

    def make_actual(self):
        if self.actual_tasks:
            self.finish_tasks.append(self.actual_tasks.make())

    def make_correct(self):
        if self.correst_tasks:
            self.finish_tasks.append(self.correst_tasks.make())


    def __str__(self):
        return [
            self.actual_tasks.tasks,
            self.correst_tasks.tasks,
            self.finish_tasks
        ].__str__()


desk = TaskQueueDesk()
desk.new_task('Первая задача')
desk.new_task(1)
desk.new_task(3.075)
print(desk) # -> [['Первая задача', 1, 3.075], [], []]
desk.to_edit()
print(desk) # -> [[1, 3.075], ['Первая задача'], []]
desk.make_actual()
print(desk) # -> [[1, 3.075], ['Первая задача'], [1]]
desk.make_correct()
print(desk) # -> [[1, 3.075], [], [1, 'Первая задача']]