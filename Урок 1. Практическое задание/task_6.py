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


class QueueTaskClass:
    def __init__(self):
        self.basic = []
        self.modification = []
        self.solved = []

    def to_basic(self, task_id):
        self.basic.insert(0, task_id)

    def from_basic_to_solved(self):
        self.solved.insert(0, self.basic.pop())

    def from_solved_to_modification(self):
        self.modification.insert(0, self.solved.pop())

    def from_modification_to_solved(self):
        self.solved.insert(0, self.modification.pop())


if __name__ == '__main__':
    a = QueueTaskClass()
    a.to_basic(1)
    a.to_basic(2)
    a.to_basic(3)
    a.to_basic(4)

    print(a.basic)

    a.from_basic_to_solved()
    a.from_basic_to_solved()
    a.from_basic_to_solved()
    a.from_solved_to_modification()
    a.from_solved_to_modification()
    a.from_modification_to_solved()

    print(a.basic)
    print(a.solved)
    print(a.modification)
