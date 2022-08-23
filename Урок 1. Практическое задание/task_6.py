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

class TaskDesk:
    def __init__(self):
        self.base = []
        self.queue = []
        self.revision = []
        self.solved = []

    def to_base(self, task):
        self.base.append(task)

    def to_solved(self, task):
        if task in self.base:
            self.solved.append(task)
            self.base.remove(task)
        elif task in self.revision:
            self.solved.append(task)
            self.revision.remove(task)
        else:
            return print(f'Задачи {task} не найдено')

    def to_queue(self, task):   # В случае если в очереди 5 и более задач последняя задача попадает в список revison
        if task in self.base:
            self.queue.insert(0, task)
            self.base.remove(task)
        else:
            print(f'Задачи {task} не найдено')

        if len(self.queue) >= 5:
            self.revision.append(self.queue[-1])
            self.queue.pop()

    def observe(self):
        print(f'Базовый список задач: {self.base}')
        print(f'Текущая очередь: {self.queue}')
        print(f'Задачи на доработке: {self.revision}')
        print(f'Список решенных задач: {self.solved}')


b = TaskDesk()

for i in range(1, 16):
    b.to_base(f'Task {i}')

b.observe()

for i in range(1, 4):
    b.to_solved(f'Task {i}')

b.observe()

for i in range(4, 9):
    b.to_queue(f'Task {i}')

b.observe()
