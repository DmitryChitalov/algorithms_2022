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


# Создаем класс для очереди
class Queue:
    def __init__(self):
        self.items = []

    def add_(self, item):
        self.items.append(item)

    def remove_(self):
        return self.items.pop(0)

    def read_list(self):
        return '\n'.join([str(i) for i in self.items])


# Создаем класс для списка задач
class ToDoList:
    def __init__(self):
        self.in_work = Queue()
        self.revision = Queue()
        self.received = Queue()

    def tasks_list(self):
        return f"In work:\n{self.in_work.read_list()}\n\n" \
               f"\nRevision:\n{self.revision.read_list()}\n\n" \
               f"\nReceived:\n{self.received.read_list()}"

    def add_(self, item):
        self.in_work.add_(item)

    def to_revision(self):
        self.revision.add_(self.in_work.remove_())

    def to_received(self):
        self.received.add_(self.in_work.remove_())

    def rev_to_received(self):
        self.received.add_(self.revision.remove_())


todolist = ToDoList()

for i in range(0, 10):
    todolist.add_(f'Task {i}')

todolist.to_revision()
todolist.to_revision()
todolist.to_received()
todolist.rev_to_received()

print(todolist.tasks_list())
