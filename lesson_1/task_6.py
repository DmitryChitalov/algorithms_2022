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
        self.queue_tasks = QueueClass()
        self.rework_tasks = QueueClass()
        self.completed_tasks = QueueClass()

    def add_task(self, item):
        self.queue_tasks.to_queue(item)

    def rework_task(self):
        self.rework_tasks.to_queue(self.queue_tasks.from_queue())

    def completed_task(self):
        self.completed_tasks.to_queue(self.queue_tasks.from_queue())

    def completed_rework(self):
        self.completed_tasks.to_queue(self.rework_tasks.from_queue())


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.add_task('task_1')
    task_board.add_task('task_2')
    task_board.add_task('task_3')
    print(task_board.queue_tasks.elems)
    task_board.rework_task()
    task_board.completed_task()
    print(task_board.queue_tasks.elems)
    print(task_board.rework_tasks.elems)
    print(task_board.completed_tasks.elems)
    task_board.completed_rework()
    print(task_board.completed_tasks.elems)
