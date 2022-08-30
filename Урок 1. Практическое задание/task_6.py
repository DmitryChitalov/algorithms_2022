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

    def get_first(self):
        return self.elems[-1]

    def __str__(self):
        return '\n'.join(self.elems)


class TasksBoard:
    def __init__(self):
        self.waiting_tasks = QueueClass()
        self.tasks_to_correct = QueueClass()
        self.done = QueueClass()

    def new_task(self, task):
        self.waiting_tasks.to_queue(task)

    def is_done(self):
        if not self.waiting_tasks.is_empty():
            self.done.to_queue(self.waiting_tasks.from_queue())
        else:
            print("Нет текущих задач")

    def for_correction(self):
        if not self.waiting_tasks.is_empty():
            self.tasks_to_correct.to_queue(self.waiting_tasks.from_queue())
        else:
            print("Нет текущих задач")

    def is_corrected(self):
        if not self.tasks_to_correct.is_empty():
            self.done.to_queue(self.tasks_to_correct.from_queue())
        else:
            print("Нет текущих задач на доработку")


my_board = TasksBoard()
print(my_board.waiting_tasks)
for i in range(8):
    my_board.new_task(f'task № {i}')

print(my_board.waiting_tasks)
my_board.is_done()
my_board.is_done()
my_board.is_done()
my_board.for_correction()
my_board.for_correction()
my_board.for_correction()

print("Текущие задачи\n", my_board.waiting_tasks)
print('******')
print("Выполненные задачи\n", my_board.done)
print('*******')
print("Задачи на доработку\n", my_board.tasks_to_correct)

my_board.is_corrected()
my_board.is_done()
my_board.is_done()
my_board.is_done()

print("Текущие задачи\n", my_board.waiting_tasks)
print('******')
print("Выполненные задачи\n", my_board.done)
print('*******')
print("Задачи на доработку\n", my_board.tasks_to_correct)
