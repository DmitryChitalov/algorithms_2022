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

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.items])

    def pop(self):
        return self.items.pop(0)

    def add(self, item):
        self.items.append(item)


class ToDo:
    def __init__(self):
        self.working = Queue()
        self.revision = Queue()
        self.done = Queue()

    def __str__(self):
        return f"Working:\n{self.working}\n\n\nRevision:\n{self.revision}\n\n\nDone:\n{self.done}"
    def add(self, item):
        self.working.add(item)
    def cur_to_rev(self):
        self.revision.add(self.working.pop())
    def cur_to_done(self):
        self.done.add(self.working.pop())
    def rev_to_done(self):
        self.done.add(self.revision.pop())

a = ToDo()

for i in range(1, 20):
    a.add(f'task {i}')

a.cur_to_rev()
a.cur_to_rev()
a.cur_to_done()
a.rev_to_done()

print(a)