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


class Quene:
    def __init__(self):
        self.lst = []

    def in_quene(self, el):
        self.lst.insert(0, el)

    def out_quene(self):
        return self.lst.pop()


class TaskBoard:
    def __init__(self):
        self.basic_quene = Quene()
        self.rev_quene = Quene()
        self.complete_tasks = []

    def new_task(self, task):
        self.basic_quene.in_quene(task)

    def done_tasks(self):  # перевод решенной задачи из базовой очереди в список решенных
        task = self.basic_quene.out_quene()
        self.complete_tasks.append(task)

    def rev_tasks(self):  # перевод задачи из базовой очереди в очередь на доработку
        task = self.basic_quene.out_quene()
        self.rev_quene.in_quene(task)

    def rev_basic_tasks(self):  # перевод откорректированной задачи из очереди на доработку в базовую очередь
        task = self.rev_quene.out_quene()
        self.basic_quene.in_quene(task)

    def complete_task(self):
        task = self.basic_quene.out_quene()
        self.complete_tasks.append(task)


plan = TaskBoard()
plan.new_task('Выучить стих')
plan.new_task('Покормить кота')
plan.rev_tasks()
plan.rev_basic_tasks()
plan.complete_task()