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


class TaskBoard():
    def __init__(self):
        self.tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.tasks_modifications = []
        self.solved_tasks = []

    def solved(self):
        '''Решенные задачи, которые отправляются из основного списка задач'''
        self.solved_tasks.append(self.tasks.pop())

    def modificate(self):
        '''Задачи которые отправляются в список задач для доработки'''
        self.tasks_modifications.append(self.tasks.pop())

    def solved_modification(self):
        '''Задачи отправляются в список решенных, из списка задач на доработку'''
        self.solved_tasks.append(self.tasks_modifications.pop())

    def __str__(self):
        return f'{self.tasks} - Оставшиеся задачи\n{self.tasks_modifications} - задачи на доработку \n{self.solved_tasks} - решенные задачи'


tasks = TaskBoard()
tasks.modificate()
tasks.modificate()
tasks.modificate()
tasks.modificate()
tasks.modificate()
tasks.modificate()
tasks.solved()
tasks.solved()
tasks.solved()
tasks.solved()
tasks.solved()
tasks.solved_modification()
tasks.solved_modification()
tasks.solved_modification()
tasks.solved_modification()

print(tasks)