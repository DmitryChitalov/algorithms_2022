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
        self.cur_queue = QueueClass()
        self.revision_quere = QueueClass()
        self.log = []

    def resolve_task(self):
        # закрывается задача и добавляется в лог
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):
        # отправляется на доработку
        task = self.cur_queue.from_queue()
        self.revision_quere.to_queue(task)

    def to_current_queue(self, item):
        #задача добавляется в текущие
        self.cur_queue.to_queue(item)

    def from_revision(self):
        # из доработки в текущую очередь
        task = self.revision_quere.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        # текущая задача
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def revision_task(self):
        # текущая задача
        return self.revision_quere.elems[len(self.revision_quere.elems) - 1]

TB = TaskBoard()

TB.to_current_queue('task1')
TB.to_current_queue('task2')
TB.to_current_queue('task3')
print ('Текущая задача: ', TB.current_task())
TB.to_revision_task()
print ('Текущая задача: ', TB.current_task())
print ('Задача на доработке: ', TB.revision_task())
TB.resolve_task()
print ('Текущая задача: ', TB.current_task())
print('Завершенная задача в логе:', TB.log)
TB.from_revision()
print ('Текущая задача: ', TB.current_task())