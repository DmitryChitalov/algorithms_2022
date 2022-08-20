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


class TasksQueue:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return self.queue_list == []

    def add_to(self, item):
        self.queue_list.insert(0, item)

    def get_from(self):
        return self.queue_list.pop()

    def size(self):
        return len(self.queue_list)


class TasksBoard:
    def __init__(self):
        self.base_queue = TasksQueue()
        self.rework_queue = TasksQueue()
        self.completed_tasks = []

    def add_to_base(self, task):
        self.base_queue.add_to(task)

    def complete_task(self, rework=False):
        if rework:
            if not self.rework_queue.is_empty():
                self.completed_tasks.append(self.rework_queue.get_from())
            else:
                print('Очередь пуста')
        else:
            if not self.base_queue.is_empty():
                self.completed_tasks.append(self.base_queue.get_from())
            else:
                print('Очередь пуста')

    def task_to_rework(self):
        if not self.base_queue.is_empty():
            self.rework_queue.add_to(self.base_queue.get_from())
        else:
            print('Очередь пуста')

    def current_task(self):
        if not self.base_queue.is_empty():
            return self.base_queue.queue_list[self.base_queue.size() - 1]
        else:
            return []

    def current_rework(self):
        if not self.rework_queue.is_empty():
            return self.rework_queue.queue_list[self.rework_queue.size() - 1]
        else:
            return []

    def get_completed(self):
        return self.completed_tasks


if __name__ == '__main__':
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6']

    my_task_board = TasksBoard()

    for el in tasks:
        my_task_board.add_to_base(el)

    print('Базовая очередь')
    print(my_task_board.base_queue.queue_list, '\n')

    my_task_board.task_to_rework()
    my_task_board.task_to_rework()
    print('Отправка на доработку двух первых задач')
    print('Базовая очередь', my_task_board.base_queue.queue_list)
    print('Очередь на доработку', my_task_board.rework_queue.queue_list)
    print('\n')
    my_task_board.complete_task(rework=True)
    print('Завершение задачи из доработки')
    print('Очередь на доработку', my_task_board.rework_queue.queue_list)
    print('Список завершенных задач', my_task_board.get_completed())
