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


class MyQueue:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []

    def to_queue(self, task):
        self.base.insert(-1, task)

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_to_base(self):
        self.base.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    tasks = MyQueue()
    tasks.to_queue('Задача_1')
    tasks.to_queue('Задача_2')
    tasks.to_queue('Задача_3')
    print(tasks.base)
    print(tasks.size())
    tasks.to_solved()
    print(tasks.solved)
    tasks.to_revision()
    print(tasks.revision)
    tasks.return_to_base()
    print(tasks.revision)
    print(tasks.base)
