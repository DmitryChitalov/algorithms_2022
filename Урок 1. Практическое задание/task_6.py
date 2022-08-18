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

import inspect


class Queue():
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        return self.queue

    def add(self, item):
        self.queue.append(item)
        return self.queue

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
        return self.queue

    def get(self):
        return self.queue[-1]

    def change_queue(self, other):
        if type(other) is Queue:
            self.queue.append(other.get())
            other.remove()
            return True
        else:
            return False


class Trello:
    def __init__(self):
        self.waiting = Queue()
        self.__setattr__(f"add_waiting", self.__add_to__)

        self.revision = Queue()
        self.__setattr__(f"add_revision", self.__add_to__)

        self.progress = Queue()
        self.__setattr__(f"add_progress", self.__add_to__)

        self.accomplished = Queue()
        self.__setattr__(f"add_accomplished", self.__add_to__)

    def add_board(self, name):
        if type(name) is str:
            name = name.split('\\')[0]
            self.__setattr__(name, Queue())
            self.__setattr__(f"add_{name}", self.__add_to__)
            return self.__getattribute__(name)
        else:
            return False

    def remove_board(self, name):
        self.__setattr__(name, False)

    def __add_to__(self, item):
        func_name = inspect.stack()[1].code_context[0].split('\n')[0]
        board_name = func_name.split('add_')[1].split('(')[0]
        queue = self.__getattribute__(board_name)
        queue.add(item)

    def change_queue(self, current, other):
        if type(current) is Queue and type(other) is Queue:
            current.add(other.get())
            other.remove()
            return True
        else:
            return False

    def to_revision(self):
        self.revision.add(self.progress.get())
        self.progress.remove()

    def from_revision(self):

        self.progress.add(self.revision.get())
        self.revision.remove()

    def to_do(self):
        self.progress.add(self.waiting.get())
        self.waiting.remove()

    def resolve(self):
        self.progress.remove()


boards = Trello()
boards.add_waiting('item')
boards.add_waiting('item1')
boards.add_waiting('item1')
boards.add_waiting('item2')
boards.add_waiting('item2')
boards.add_waiting('item3')
boards.add_waiting('item3')
boards.to_do()
boards.to_do()
boards.to_do()
boards.to_revision()
boards.to_revision()
boards.resolve()
boards.resolve()
boards.add_board('name')
boards.remove_board('name')
print(boards)
