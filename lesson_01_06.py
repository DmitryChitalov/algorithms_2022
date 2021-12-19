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


class BoardQueue:
    def __init__(self):
        self.basic_board = []
        self.completed_board = []
        self.rework_board = []

    def in_basic(self, task):
        self.basic_board.insert(0, task)
        return print(f'Current basic tasks: {self.basic_board}')

    def for_rework(self):
        self.rework_board.insert(0, self.basic_board.pop())
        return print(f'Tasks for rework: {self.rework_board}')

    def completed(self):
        self.completed_board.insert(0, self.basic_board.pop())
        return print(f'Completed tasks: {self.completed_board}')

    def reworked(self):
        self.basic_board.insert(0, self.rework_board.pop())
        return print(f'One tasks fixed and moved to basic board: {self.basic_board}')


a = BoardQueue()
a.in_basic('task_1')
a.in_basic('task_2')
a.in_basic('task_3')

a.for_rework()
a.completed()
a.reworked()
