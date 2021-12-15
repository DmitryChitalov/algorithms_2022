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

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def print_queue(self):
        print(self.elems)


class Board:
    def __init__(self):
        self.types = {'Базовая очередь': QueueClass(), 'Решенные задачи': QueueClass(), 'На доработку':  QueueClass()}

    def add_task(self, task):
        self.types['Базовая очередь'].to_queue(task)

    def move(self, from_q, to_q):
        self.types[to_q].to_queue(self.types[from_q].from_queue())

    def solve(self):
        self.move('Базовая очередь', 'Решенные задачи')

    def think(self):
        self.move('Базовая очередь', 'На доработку')

    def finish(self):
        self.move('На доработку', 'Решенные задачи')

    def print_tasks(self):
        for i in self.types.keys():
            print(i)
            self.types[i].print_queue()


tasks = Board()
tasks.add_task('task_1')
tasks.add_task('task_2')
tasks.add_task('task_3')
tasks.add_task('task_4')
tasks.add_task('task_5')
tasks.add_task('task_6')
tasks.solve()
tasks.think()
tasks.finish()
tasks.think()
tasks.think()

tasks.print_tasks()
