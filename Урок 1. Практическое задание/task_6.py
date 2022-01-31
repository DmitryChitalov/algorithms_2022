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


class Board:
    def __init__(self):
        self.tasks = []
        self.modification = []
        self.done = []

    def size(self):
        task_board = {
            'Новых задач': len(self.tasks),
            'Задачи на доработке': len(self.modification),
            'Выполненные задачи': len(self.done)
        }
        return task_board

    def add_task(self, task):
        self.tasks.insert(0, task)

    def get_task(self):
        return self.tasks.pop()

    def done_task(self, task):
        self.done.insert(0, task)

    def task_to_done(self):
        return self.done.pop()

    def task_modification(self, task):
        self.modification.insert(0, task)

    def task_to_modification(self):
        return self.modification.pop()


board = Board()
print(board.size())

board.add_task(f'Задача № 1')

board.add_task(f'Задача № 2')

board.add_task(f'Задача № 3')

print(board.size())

task_to_done = board.get_task()
print(task_to_done)
board.done_task(task_to_done)

print(board.size())

task_to_done_2 = board.get_task()
print(task_to_done_2)
board.done_task(task_to_done_2)

print(board.size())


task_to_modification = board.task_to_done()
print(task_to_modification)
board.task_modification(task_to_modification)

print(board.size())

correct_task = board.task_to_modification()
print(correct_task)
board.done_task(correct_task)

print(board.size())

task_to_done_3 = board.get_task()
print(task_to_done_3)
board.done_task(task_to_done_3)

print(board.size())
