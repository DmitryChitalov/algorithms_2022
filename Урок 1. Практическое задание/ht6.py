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
        self.rev_queue = QueueClass()
        self.compl_queue = []

    def to_current_queue(self, task): # добавить задачу в текущие
        self.cur_queue.to_queue(task)

    def cur_to_compl_task(self): # из текущей в завершенные
        task = self.cur_queue.from_queue()
        self.compl_queue.append(task)

    def rev_to_compl_task(self): # из доработки в завершенные
        task = self.rev_queue.from_queue()
        self.compl_queue.append(task)

    def to_revision_task(self): # из текущей в доработку
        task = self.cur_queue.from_queue()
        self.rev_queue.to_queue(task)

    def from_revision(self): # из доработки в текущую
        task = self.rev_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        return self.cur_queue.elems[-1]

    def current_revision_task(self):
        return self.rev_queue.elems[-1]

if __name__ == '__main__':
    new_obj = TaskBoard()
    new_obj.to_current_queue('first')
    new_obj.to_current_queue('second')
    new_obj.to_current_queue('third')
    new_obj.to_current_queue('fourth')
    new_obj.to_revision_task()
    new_obj.to_revision_task()

    new_obj.rev_to_compl_task()
    new_obj.cur_to_compl_task()

    print(new_obj.current_task())
    print(new_obj.current_revision_task())
    print(new_obj.compl_queue)

