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


class TurnClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_turn(self, item):
        self.elems.insert(0, item)

    def from_turn(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.cur_turn = TurnClass()    # Базовая очередь
        self.revision_turn = TurnClass()   # очередь на доработку
        self.log = []  # Список решенных задач

    def resolve_task(self):
        """Закрываем текущую задачу и добавляем в решенные"""
        task = self.cur_turn.from_turn()
        self.log.append(task)

    def to_revision_task(self):
        """Отправляем текущую задачу на доработку"""
        task = self.cur_turn.from_turn()
        self.revision_turn.to_turn(task)

    def to_current_turn(self, item):
        """Добавляем задачу в текущие"""
        self.cur_turn.to_turn(item)

    def from_revision(self):
        """Возвращаем задачу из доработки в текущую очередь"""
        task = self.revision_turn.from_turn()
        self.cur_turn.to_turn(task)

    def current_task(self):
        """Текущая задача"""
        return self.cur_turn.elems[len(self.cur_turn.elems) - 1]

    def current_revision(self):
        """Задача в доработке"""
        return self.revision_turn.elems[len(self.revision_turn.elems) - 1]


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_current_turn("Task1")
    task_board.to_current_turn("Task2")
    task_board.to_current_turn("Task3")
    print(task_board.cur_turn.elems)
    print(task_board.current_task())
    task_board.to_revision_task()
    task_board.resolve_task()
    task_board.from_revision()
    print(task_board.cur_turn.elems)
    print(task_board.current_task())
    print(task_board.log)
