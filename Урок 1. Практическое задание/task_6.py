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

import random


class Task:
    def __init__(self):
        num = random.sample(range(1, 99), 10)
        self.task_base = num
        self.task_rework = []
        self.task_complete = []
        self.task_add_from_task_base()

    def task_add_from_task_base(self):
        while len(self.task_base) != 0:
            task = self.task_base.pop(0)
            print('Задача', task)
            answer = input('Решена задача? ')
            if answer == 'y':
                self.task_complete.append(task)
                print('Решенные задачи', self.task_complete)
            if answer == 'n':
                self.task_rework.append(task)
                print('Задачи отправленные на корректировку', self.task_rework)
        self.task_add_from_rework()

    def task_add_from_rework(self):
        while len(self.task_rework):
            task = self.task_rework.pop(0)
            print(task)
            answer = input('Задача исправлена?' )
            if answer == 'y':
                self.task_complete.append(task)
                print('Решенные задачи', self.task_complete)
        print('Все задачи выполнены')


x = Task()
