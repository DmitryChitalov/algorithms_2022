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
        """Проверка на пустоту"""
        return self.elems == []

    def to_queue(self, item):
        """Вставить в очередь"""
        self.elems.insert(0, item)

    def from_queue(self):
        """Взять из очереди"""
        return self.elems.pop()

    def size(self):
        """Размер очереди"""
        return len(self.elems)

    def show_task(self):
        return self.elems


class TaskBoard:

    def __init__(self):
        self.main = QueueClass()
        self.mod = QueueClass()
        self.decided = QueueClass()

    def main_to_decided(self):
        """Из главной в решенные"""
        self.decided.to_queue(self.main.from_queue())

    def main_to_mod(self):
        """Из главной на доработку"""
        self.mod.to_queue(self.main.from_queue())

    def mod_to_decided(self):
        """Из доработки в решенные"""
        self.decided.to_queue(self.mod.from_queue())


if __name__ == '__main__':

    board = TaskBoard()

    print(board.main.is_empty())

    for i in range(1, 10 + 1):
        board.main.to_queue(i)

    print(board.main.show_task())
    board.main_to_mod()
    board.main_to_mod()
    board.main_to_mod()
    board.main_to_decided()
    board.mod_to_decided()
    board.mod_to_decided()
    print(board.main.show_task())
    print(board.mod.show_task())
    print(board.decided.show_task())
