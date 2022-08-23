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
        self.main_queue = []
        self.rmk_queue = []
        self.completed_queue = []

    def add_tasks(self, tasks):
        for i in tasks:
            self.main_queue.insert(0, i)


    def finalize(self, task_num):
        for i in range(task_num):
            self.rmk_queue.insert(0, self.main_queue.pop())

    def complete(self, task_num, queue_type):
        if queue_type == 'main':
            for i in range(task_num):
                self.completed_queue.insert(0, self.main_queue.pop())
        elif queue_type == 'rmk':
            for i in range(task_num):
                self.completed_queue.insert(0, self.rmk_queue.pop())

    def __str__(self):
        return f'{str(self.main_queue)}\n{str(self.rmk_queue)}\n{str(self.completed_queue)}'

queues = TaskBoard()
queues.add_tasks(['task1', 'task2', 'task3'])
print(queues)
queues.add_tasks(['task4', 'task5'])
print(queues)
queues.finalize(2)
print(queues)
queues.complete(1, 'main')
print(queues)
queues.complete(1, 'rmk')
print(queues)


