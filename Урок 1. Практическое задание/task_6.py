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
import random


class Queue:

    def __init__(self):
        self.queue_task = []
        self.tasks_solved = []

    def add_task(self, task):
        self.queue_task.append(task)

    def solve_task(self):
        case = random.randint(0, 2)
        if case:
            self.tasks_solved.append(self.queue_task.pop(0))
        else:
            self.queue_task.append(self.queue_task.pop(0))


tasks = Queue()

for task in range(30):
    tasks.add_task(task)
print(tasks.queue_task)

while tasks.queue_task:
    tasks.solve_task()
print(tasks.tasks_solved)
