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
        self.items = []

    def clear(self):
        return self.items == []

    def append(self, item):
        self.items.insert(0, item)

    def get_item(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class TaskBoard:
    def __init__(self):
        self.current_queue = QueueClass()  # Базовая
        self.revision_queue = QueueClass()  # Доработка
        self.finished_tasks = []  # Решенные задачи

    def solve_task(self):
        """ Добавляем в решенные задачи"""
        task = self.current_queue.get_item()
        self.finished_tasks.append(task)

    def send_to_revision(self):
        """Отправляем на доработку текущую задачу"""
        task = self.current_queue.get_item()
        self.revision_queue.append(task)

    def send_to_current(self, item):
        """ Добавляем задачу в текущую"""
        self.current_queue.append(item)

    def from_revision(self):
        """ Из доработки в текущую очередь"""
        task = self.revision_queue.get_item()
        self.current_queue.append(task)

    def current_task(self):
        """Текущая задача"""
        return self.current_queue.items[len(self.current_queue.items) - 1]

    def on_revision(self):
        """ Задачи, находящиеся в доработке"""
        return self.revision_queue.items[len(self.revision_queue.items) - 1]


if __name__ == '__main__':
    tasks = TaskBoard()
    tasks.send_to_current('Make a bed')
    tasks.send_to_current('Do the dishes')
    tasks.send_to_current('Walk a dog')
    tasks.send_to_current('Do homework')
    print(tasks.current_queue.items)
    print(tasks.current_task())
    tasks.send_to_revision()
    tasks.solve_task()
    # tasks.from_revision()
    print(tasks.current_queue.items)
    print(tasks.current_task())
    print(tasks.on_revision())

# Можно добавить еще условие, чтобы не было ошибки index out of range, когда в списках пусто.
