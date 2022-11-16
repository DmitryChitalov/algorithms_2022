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


class Column:
    def __init__(self):
        self.items = []

    def is_not_empty(self):
        return len(self.items) != 0

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, item):
        self.items.insert(0, item)

    def pop_item(self):
        if self.is_not_empty():
            return self.items.pop()
        return ('Задачь нет')

    def last_task(self):
        if (self.is_empty()):
            return self.items[-1]
        return ('Задач нет')

    def size(self):
        return len(self.items)


class Kanban:
    def __init__(self):
        self.in_progress = Column()  # IN_PROGRESS
        self.to_fix = Column()       # TO_FIX
        self.done = Column()         # DONE

    def done_task(self):
        task = self.in_progress.pop_item()
        self.done.add_item(task)

    def to_fix_task(self):
        task = self.in_progress.pop_item()
        self.to_fix.add_item(task)

    def to_in_progress(self, item):
        self.in_progress.add_item(item)

    def from_fix(self):
        task = self.to_fix.pop_item()
        self.in_progress.add_item(task)

    def current_task(self):
        return self.in_progress.last_task()

    def current_fix_task(self):
        return self.to_fix.last_task()


if __name__ == '__main__':
    task_board = Kanban()
    for i in range(1, 4):
        task_board.to_in_progress(f"Task {i}")
    print(*task_board.in_progress.items)
    print(task_board.current_task())
    task_board.to_fix_task()
    task_board.done_task()
    task_board.from_fix()
    print(*task_board.in_progress.items)
    print(*task_board.to_fix.items)
    print(task_board.current_task())
    print(*task_board.done.items)

