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

    def print_out(self):
        return self.elems


class TaskQueueClass:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.done_queue = QueueClass()
        self.re_queue = QueueClass()

    def to_cur_queue(self, item):
        self.cur_queue.to_queue(item)

    def from_cur_to_done(self):
        self.done_queue.to_queue(self.cur_queue.from_queue())

    def from_cur_to_re(self):
        self.re_queue.to_queue(self.cur_queue.from_queue())

    def from_re_to_done(self):
        self.done_queue.to_queue(self.re_queue.from_queue())

    def get_cur_queue(self):
        return self.cur_queue.print_out()

    def get_done_queue(self):
        return self.done_queue.print_out()

    def get_re_queue(self):
        return self.re_queue.print_out()


if __name__ == "__main__":
    my_task_queue = TaskQueueClass()
    for i in range(5):
        my_task_queue.to_cur_queue(f'Задача {i}')
    print("Текущие задачи :", my_task_queue.get_cur_queue())
    print("Выполненные задачи :", my_task_queue.get_done_queue())
    print("Задачи на доработку :", my_task_queue.get_re_queue())
    print("2 задачи выполнено")
    print("1 задача нуждается в доработке")
    my_task_queue.from_cur_to_done()
    my_task_queue.from_cur_to_done()
    my_task_queue.from_cur_to_re()
    print("Текущие задачи :", my_task_queue.get_cur_queue())
    print("Выполненные задачи :", my_task_queue.get_done_queue())
    print("Задачи на доработку :", my_task_queue.get_re_queue())
    my_task_queue.from_re_to_done()
    my_task_queue.from_cur_to_re()
    print("1 задача доработана")
    print("1 задача нуждается в доработке")
    print("Текущие задачи :", my_task_queue.get_cur_queue())
    print("Выполненные задачи :", my_task_queue.get_done_queue())
    print("Задачи на доработку :", my_task_queue.get_re_queue())
