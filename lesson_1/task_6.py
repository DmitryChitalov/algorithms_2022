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
        self.current_queue = QueueClass()
        self.rework_queue = QueueClass()
        self.log = []

    def complete_task(self):
        task = self.current_queue.from_queue()
        self.log.append(task)

    def to_rework_task(self):
        task = self.current_queue.from_queue()
        self.rework_queue.to_queue(task)

    def to_current_queue(self, el):
        self.current_queue.to_queue(el)

    def from_rework(self):
        task = self.rework_queue.from_queue()

    def current_task(self):
        return self.current_queue.elems[len(self.current_queue.elems) - 1]

    def current_rework(self):
        return self.rework_queue.elems[len(self.rework_queue.elems) - 1]


if __name__ == '__main__':
    task_bord = TaskBoard()
    task_bord.to_current_queue('Task1')
    task_bord.to_current_queue('Task2')
    task_bord.to_current_queue('Task3')
    task_bord.to_current_queue('Task4')
    task_bord.to_current_queue('Task5')
    print(task_bord.current_queue.size())  # -> 5
    print(task_bord.current_queue.elems)  # ->  ['Task5', 'Task4', 'Task3', 'Task2', 'Task1']
    print(task_bord.current_task())  # ->  Task1
    task_bord.to_rework_task()
    print(task_bord.rework_queue.size())  # -> 1
    task_bord.complete_task()
    task_bord.from_rework()
    print(task_bord.current_queue.elems)  # -> ['Task5', 'Task4', 'Task3']
    print(task_bord.current_task())  # -> Task3
    print(task_bord.log)  # -> ['Task2']
    print(task_bord.current_queue.size())  # ->3
