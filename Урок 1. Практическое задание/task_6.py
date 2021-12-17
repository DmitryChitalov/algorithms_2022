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
import math


class Task:
    def __init__(self, data, solver, refixer):
        self.data = data
        self.result = None
        self.solver = solver
        self.refixer = refixer

    def solve(self):
        try:
            self.result = self.solver(self.data)
            return True
        except:
            return False

    def refix(self):
        try:
            self.result = self.refixer(self.data)
            return True
        except:
            return False


class TaskBoard:
    def __init__(self):
        self.pending = []
        self.solved = []
        self.incompleted = []

    def submit(self, task):
        self.pending.append(task)

    def solve(self):
        # solve pending tasks first
        while self.pending:
            t = self.pending.pop(0)
            if t.solve():
                self.solved.append(t)
            else:
                self.incompleted.append(t)
        # now try to re-fix incomplete tasks
        while self.incompleted:
            t = self.incompleted.pop(0)
            if t.refix():
                self.solved.append(t)
            else:
                self.incompleted.append(t)

    def flushSolved(self):
        for t in self.solved:
            print("task solved, result ", t.result)
        self.solved = []


if __name__ == '__main__':
    board = TaskBoard()

    board.submit(Task(4, math.sqrt, lambda _: "Fixer not implemented"))
    board.submit(Task(123, math.log, lambda _: "Fixer not implemented"))

    board.solve()
    board.flushSolved()
