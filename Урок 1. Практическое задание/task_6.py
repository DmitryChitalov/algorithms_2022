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
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class Taskboard:
    def __init__(self):
        self.base_task = QueueClass()
        self.task_before_done = QueueClass()
        self.done_task = [[]]

    def to_base_task(self, el):
        return self.base_task.to_queue(el)

    def to_task_before_done(self):
        task = self.base_task.from_queue()
        self.task_before_done.to_queue(task)

    def to_done_task(self):
        task = self.base_task.from_queue()
        self.done_task.append(task)

    def from_task_before_done_to_base_task(self):
        task = self.task_before_done.from_queue()
        self.base_task.to_queue(task)

    def base_task(self):
        return self.base_task.elems[len(self.base_task.elems) - 1]

    def done_task(self):
        return self.done_task.elems[len(self.done_task.elems) - 1]

    def task_before_done(self):
        return self.task_before_done[len(self.task_before_done.elems) - 1]


if __name__ == "__main__":
    trello = Taskboard()

    trello.to_base_task("start")
    trello.to_base_task("start2")
    trello.to_base_task("start3")
    trello.to_task_before_done()
    print(trello.task_before_done)
