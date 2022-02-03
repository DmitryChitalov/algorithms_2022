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

class TaskBoard():
    def __init__(self):
        self.basic = []
        self.solved_problems = []
        self.revision = []

    def send_to_base_queue(self, task):  # все задачи изначально добавляются в базовую очередь
        self.basic.append(task)

    def show_tasks(self, what):
        if what == 'basic':
            print(f'Задачи: {self.basic}')
        elif what == 'revision':
            print(f'Задачи на доработку: {self.revision}')
        elif what == 'resolved':
            print(f'Решённые задачи: {self.solved_problems}')
    # что бы посмотреть задачи в скобках указываем нужный список задач

    def send_for_revision(self, num):    # смотрим, какие есть задачи и выбираем из списка на доработку
        i = self.basic.pop(num-1)
        self.revision.append(i)

    def tu_solved_problems(self, num):      # смотрим, какие есть задачи и отправляем в решённые
        i = self.basic.pop(num-1)
        self.solved_problems.append(i)

    def remove_from_revision(self, num):
        i = self.revision.pop(num - 1)
        self.solved_problems.append(i)



task = TaskBoard()
task.send_to_base_queue('сделать финансовый отчёт')
task.send_to_base_queue('провести планёрку')
task.show_tasks('basic')
task.send_for_revision(2)
task.show_tasks('revision')
task.show_tasks('basic')
task.tu_solved_problems(1)
task.show_tasks('basic')
task.show_tasks('resolved')
task.remove_from_revision(1)
task.show_tasks('revision')
task.show_tasks('resolved')
