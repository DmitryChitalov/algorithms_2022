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
        self.elems = []

    def __str__(self):
        return 'Queue:\n' + '\n'.join([' '.join([str(y) for y in self.elems])])

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        if item is not None:
            self.elems.insert(0, item)

    def from_queue(self):
        if self.is_empty():
            return None
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class KanbanBoards:
    def __init__(self):
        self.open = QueueClass()  # 'Open' - Еще не начатая работа
        self.in_progress = QueueClass()  # 'In progress' - В работе
        self.code_review = QueueClass()  # 'Code review' - Проверка кода
        self.done = QueueClass()  # 'Done' - Завершено
        self.todo = {
            'create': lambda x: self.open.to_queue(x),  # create work
            'start': lambda _: self.in_progress.to_queue(self.open.from_queue()),  # start progress
            'ready': lambda _: self.code_review.to_queue(self.in_progress.from_queue()),  # ready for review
            'cr_pass': lambda _: self.done.to_queue(self.code_review.from_queue()),  # cod review passed
            'reopen': lambda _: self.open.to_queue(self.done.from_queue()),  # reopen work (back)
            'cr_failed': lambda _: self.in_progress.to_queue(self.code_review.from_queue()),  # code review failed
            'stop': lambda _: self.open.to_queue(self.in_progress.from_queue()),  # stop progress (back)
            'unknown_todo': lambda _: False
        }

    def __str__(self):
        s = [
            f"       open: {''.join([','.join([str(y) for y in self.open.elems])])}",
            f"in_progress: {''.join([','.join([str(y) for y in self.in_progress.elems])])}",
            f"code_review: {''.join([','.join([str(y) for y in self.code_review.elems])])}",
            f"       done: {''.join([','.join([str(y) for y in self.done.elems])])}"
        ]
        return '\n'.join([str(y) for y in s])

    def create_work(self, item):
        self.todo.get('create', 'unknown_todo')(item)

    def change_status(self, what_todo):
        self.todo.get(what_todo, 'unknown_todo')('')


task_board = KanbanBoards()
print("1. заполняем доску задач 'open' task1...task14")
_ = [task_board.create_work(f'task_{x}') for x in range(15)]
print(task_board)
print("2. Первые 7 задач в активную работу 'start progress'")
_ = [task_board.change_status('start') for _ in range(7)]
print(task_board)
print("3. Первые 5 задач на проверку кода 'ready for review'")
_ = [task_board.change_status('ready') for _ in range(5)]
print(task_board)
print("4. Первые 2 задачи задача завершено 'done'")
_ = [task_board.change_status('cr_pass') for _ in range(2)]
print(task_board)
print("5. Первые 2 задач на доработку 'code review failed'")
_ = [task_board.change_status('cr_failed') for _ in range(2)]
print(task_board)
print("6. задача завершена 'done'")
_ = [task_board.change_status('cr_pass') for _ in range(2)]
print(task_board)
print("7. приостановить активную работу 2 задач 'stop progress'")
_ = [task_board.change_status('stop') for _ in range(2)]
print(task_board)
