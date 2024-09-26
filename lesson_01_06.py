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


class QueueClass:

    def __init__(self):
        self.tasks = []

    def is_empty(self):
        if self.tasks == []:
            return print('Queue is empty')
        else:
            return print('Queue doesn\'t empty')

    def to_queue(self, task):
        return self.tasks.insert(0, task)

    def from_queue(self):
        return self.tasks.pop()

    def size(self):
        return print(f'{len(self.tasks)} item(s) in queue')


class Board:

    def __init__(self):
        self.main_board = QueueClass()
        self.rework_board = QueueClass()
        self.completed_board = QueueClass()

    def to_main_board(self, item):
        self.main_board.to_queue(item)
        return print(f'{item} added to main board')

    def to_rework(self):
        self.item_to_rework = self.main_board.from_queue()
        self.rework_board.to_queue(self.item_to_rework)
        return print(f'{self.item_to_rework} added to rework board')

    def reworked(self):
        self.reworked_item = self.rework_board.from_queue()
        self.main_board.to_queue(self.reworked_item)
        return print(f'{self.reworked_item} was reworked and added to main board')

    def completed(self):
        self.completed_item = self.main_board.from_queue()
        self.completed_board.to_queue(self.completed_item)
        return print(f'{self.completed_item} added to completed board')


a = Board()

a.to_main_board('task_1')
a.to_main_board('task_2')
a.to_main_board('task_3')
a.to_main_board('task_4')
a.to_main_board('task_5')
a.to_main_board('task_6')

a.main_board.is_empty()
a.main_board.size()
a.to_rework()
a.rework_board.size()
a.to_rework()
a.completed()
a.reworked()
