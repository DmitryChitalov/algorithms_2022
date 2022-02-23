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
        self.unsolved = []  # нерешенные новые задачи
        self.solved = []  # решенные задачи
        self.resolved = []  # задачи на доработку

    def is_empty_unsolved(self):  # есть ли нерешенные задачи
        return self.unsolved == []

    def size_unsolved(self):  # число нерешенных задач
        return len(self.unsolved)

    def to_unsolved(self, item):  # добавить новою задачу
        self.unsolved.insert(0, item)

    def from_unsolved_to_solved(self):  # перевести задачу из нерешенных в решенные
        if len(self.unsolved) > 0:
            self.solved.insert(0, self.unsolved.pop())
        else:
            print('Нет доступных нерешенных задач')

    def is_empty_solved(self):  # есть ли решенные задачи
        return self.solved == []

    def size_solved(self):  # число решенных задач
        return len(self.solved)

    def from_solved_to_resolved(self):  # перевести задачу из решенных в задачи на доработку
        if len(self.solved) > 0:
            self.resolved.insert(0, self.solved.pop())
        else:
            print('Нет доступных решенных задач')

    def is_empty_resolved(self):  # есть ли задачи на доработку
        return self.solved == []

    def size_resolved(self):  # число задач на доработку
        return len(self.resolved)

    def from_resolved_to_solved(self):  # перевести задачу из доработки в решенные
        if len(self.resolved) > 0:
            self.solved.insert(0, self.resolved.pop())
        else:
            print('Нет доступных задач на доработку')

    def from_solved(self):  # удалить однозначно решенную задачу
        if len(self.solved) > 0:
            return self.solved.pop()
        else:
            print('Нет доступных решенных задач')



if __name__ == '__main__':

    TB_OBJ = TaskBoard()

    print(TB_OBJ.is_empty_unsolved())
    print(TB_OBJ.is_empty_solved())
    print(TB_OBJ.is_empty_resolved())

    TB_OBJ.to_unsolved(1)
    TB_OBJ.to_unsolved(2)
    TB_OBJ.to_unsolved(3)
    TB_OBJ.to_unsolved(4)
    TB_OBJ.to_unsolved(5)
    TB_OBJ.to_unsolved(6)

    print(TB_OBJ.is_empty_unsolved())
    print(TB_OBJ.is_empty_solved())
    print(TB_OBJ.is_empty_resolved())

    print(TB_OBJ.size_unsolved())

    print(TB_OBJ.from_unsolved_to_solved())

    print(TB_OBJ.size_unsolved())

    print(TB_OBJ.size_solved())