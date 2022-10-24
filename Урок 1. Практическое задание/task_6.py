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


class Board_of_Tasks:
    def __init__(self):
        self.all_tasks = QueueClass()
        self.in_work_tasks = QueueClass()
        self.finish_tasks = []

    def add_to_all_tasks(self, item):
        """наполнение базовой очереди"""
        self.all_tasks.to_queue(item)

    def from_all_tasks_to_in_work_tasks(self):
        """с базовой в очередь на доработку"""
        task = self.all_tasks.from_queue()
        self.in_work_tasks.to_queue(task)

    def from_all_tasks_to_finish_tasks(self):
        """с базовой очереди в список завершенных"""
        task = self.all_tasks.from_queue()
        self.finish_tasks.append(task)

    def from_in_work_tasks_to_finish_tasks(self):
        """с очереди на доработку в список завершенных"""
        task = self.in_work_tasks.from_queue()
        self.finish_tasks.append(task)


if __name__ == '__main__':
    board_of_tasks = Board_of_Tasks()
    board_of_tasks.add_to_all_tasks('TASK_1')
    board_of_tasks.add_to_all_tasks('TASK_2')
    board_of_tasks.add_to_all_tasks('TASK_3')
    print(board_of_tasks.all_tasks.elems)
    print(board_of_tasks.finish_tasks)
    board_of_tasks.from_all_tasks_to_in_work_tasks()
    print(board_of_tasks.in_work_tasks.elems)
    board_of_tasks.from_in_work_tasks_to_finish_tasks()
    print(board_of_tasks.finish_tasks)
    board_of_tasks.from_all_tasks_to_in_work_tasks()
    print(board_of_tasks.in_work_tasks.elems)
