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
        self.cur_queue = QueueClass()  # Базовая очередь
        self.revision_queue = QueueClass()  # Очередь на доработку
        self.log = []  # Список решённых задач

    def revolve_task(self):
        """Текущая задача закрывается и добалвяется в журнал"""
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):
        """Текущая задача оптарвляется на доработку"""
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        """Добавление задачи в текущие"""
        self.cur_queue.to_queue(item)

    def from_revision(self):
        """Возврат задачи из доработки в текущую очередь"""
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        """Текущая задача"""
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]


if __name__ == '__main__':
    tb = TaskBoard()
    print(type(tb))
    tb.to_current_queue('Task1')
    print(tb.current_task())
    tb.to_current_queue('Task2')
    tb.to_current_queue('Task3')
    print(tb.current_task())
    tb.revolve_task()
    print(tb.log)
    print(tb.current_task())
    tb.to_revision_task()
    print(tb.current_task())
    tb.from_revision()
    print(tb.current_task())
