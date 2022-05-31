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


class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def to_queue(self, item):
        self.queue.insert(0, item)

    def from_queue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


class TaskBoard:

    def __init__(self):
        self.current = Queue()
        self.rework = Queue()
        self.done = []

    def __str__(self):
        return f"В работе: {self.current}\nНа доработку: {self.rework}"

    def add_new_task(self, item):
        """Добавление новой задачи"""
        self.current.to_queue(item)

    def current_task_done(self):
        """Текущая задача выполнена"""
        self.done.append(self.current.from_queue())

    def rework_task_done(self):
        """Задача доработана и выполнена"""
        self.done.append(self.rework.from_queue())

    def to_rework(self):
        """Поместить задачу в очередь на доработку"""
        self.rework.to_queue(self.current.from_queue())

    def to_current(self):
        """Из очереди на доработку переместить в текущие"""
        self.current.to_queue(self.rework.from_queue())

    def get_current_task(self):
        """Получить текущую задачу"""
        return self.current.queue[-1]

    def get_rework_task(self):
        """Получить задачу на доработку"""
        return self.rework.queue[-1]


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.add_new_task("Task #1")
    task_board.add_new_task("Task #2")
    task_board.add_new_task("Task #3")
    task_board.add_new_task("Task #4")

    print(task_board)

    print('Текущая задача: ', task_board.get_current_task())
    task_board.to_rework()
    task_board.current_task_done()
    print(task_board)
    task_board.to_current()

    print('Текущая задача: ', task_board.get_current_task())
    print('Завершены: ', task_board.done)
