"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_item(self, item):
        self.items.insert(0, item)

    def pop_item(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class TaskDesk:
    def __init__(self):
        self.main_queue = Queue()    # Основная очередь
        self.fix_queue = Queue()   # На доработку
        self.result = []  # Готовые

    def do_task(self):
        """Закрываем текущую задачу и добавляем в лог"""
        task = self.main_queue.pop_item()
        self.result.append(task)

    def to_fix_queue(self):
        """Отправляем текущую задачу на доработку"""
        task = self.main_queue.pop_item()
        self.fix_queue.add_item(task)

    def to_main_queue(self, item):
        """Добавляем задачу в текущие"""
        self.main_queue.add_item(item)

    def from_fix(self):
        """Возвращаем задачу из доработки в текущую очередь"""
        task = self.fix_queue.pop_item()
        self.main_queue.add_item(task)

    def current_task(self):
        """Текущая задача"""
        return self.main_queue.items[len(self.main_queue.items) - 1]

    def current_fix_task(self):
        """Задача в доработке"""
        return self.fix_queue.items[len(self.fix_queue.items) - 1]


if __name__ == '__main__':
    task_board = TaskDesk()
    for i in range(1,4):
        task_board.to_main_queue(f"Task {i}")
    print(*task_board.main_queue.items)
    print(task_board.current_task())
    task_board.to_fix_queue()
    task_board.do_task()
    task_board.from_fix()
    print(*task_board.main_queue.items)
    print(task_board.current_task())
    print(*task_board.result)










