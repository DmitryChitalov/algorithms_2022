"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):   # добавить элемент в начало
        self.elems.insert(0, item)

    def from_queue(self):    # удалить последний элемент
        return self.elems.pop()

    def show_queue(self):
        return self.elems[-1]

    def size(self):  # длина очереди
        return len(self.elems)

class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()  # Базовая (добавляем все задачи сюда при помощи интерфейса QueueClass())
        self.rev_queue = QueueClass()  # На доработку
        self.log = []  # Решенные

    def cur_task(self):  # показать текущую задачу из базовой очереди
        return self.cur_queue.show_queue()

    def rev_task(self):  # показать текущую задачу из очереди доработки
        return self.rev_queue.show_queue()

    def add_in_rev(self):  # перенести задачу из базовой на доработку
        self.rev_queue.to_queue(self.cur_queue.from_queue())

    def add_in_log(self):  # перенести задачу из базовой в решенную
        self.log.append(self.cur_queue.from_queue())

    def add_in_log_from_rev(self):  # перенести задачу из доработки в решенные
        self.log.append(self.rev_queue.from_queue())

    def much_add_in_log(self, count): # перенести count задач из базовой в решенную
        for _ in range(count):
            self.log.append(self.cur_queue.from_queue())



if __name__ == '__main__':
    Task = TaskBoard()
    for i in range(100):
        Task.cur_queue.to_queue(i)

