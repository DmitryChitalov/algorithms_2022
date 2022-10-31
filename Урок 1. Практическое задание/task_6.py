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


class TaskBoard:
    def __init__(self):
        self.solved = []
        self.fix = []
        self.base = []

    def from_base_to_solved(self, task):
        self.solved.append(task)
        self.base.remove(task)

    def from_base_to_fix(self, task):
        self.fix.append(task)
        self.base.remove(task)

    def from_fix_to_solved(self, task):
        self.solved.append(task)
        self.fix.remove(task)

    def from_solved_to_fix(self, task):
        self.fix.append(task)
        self.solved.remove(task)

    def check_taskboard(self):
        return self.base, self.fix, self.solved

    def add_base(self, task):
        self.base.append(task)


if __name__ == '__main__':
    tb = TaskBoard()
    tb.add_base('Решить задание номер 7')
    print(tb.check_taskboard())
    tb.from_base_to_solved('Решить задание номер 7')
    print(tb.check_taskboard())