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


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:

    def __init__(self):
        self.master = QueueClass()
        self.rework = QueueClass()
        self.done = QueueClass()

    def master_to_rework(self):
        self.rework.to_queue(self.master.from_queue())

    def rework_to_done(self):
        self.done.to_queue(self.rework.from_queue())

    def master_to_done(self):
        self.done.to_queue(self.master.from_queue())

if __name__ == '__main__':

    board = TaskBoard()
    print(board.master.is_empty())
    # qc_obj = QueueClass()
    # print(qc_obj.is_empty())  # -> True. Очередь пустая
    #
    # # помещаем объекты в очередь
    # qc_obj.to_queue('my_obj')
    # qc_obj.to_queue(4)
    # qc_obj.to_queue(True)
    #
    # print(qc_obj.is_empty())  # -> False. Очередь пустая
    #
    # print(qc_obj.size())  # -> 3
    #
    # print(qc_obj.from_queue())  # -> my_obj
    #
    # print(qc_obj.size())  # -> 2