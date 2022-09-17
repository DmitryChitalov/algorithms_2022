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

class Task_board:
    def __init__(self):
        self.elems = [[], [], []]

    def is_empty(self):
        return self.elems == []

    def to_base(self, item):
        return self.elems[0].insert(0, item)

    def from_base(self):
        return self.elems[0].pop()

    def solved(self):
        return self.elems[1].insert(0, self.elems[0].pop())

    def finalization(self):
        return self.elems[2].insert(0, self.elems[0].pop())

    def size(self):
        return len(self.elems[0]) + len(self.elems[1]) + len(self.elems[2])

if __name__ == '__main__':
    qc_obj = Task_board()
    # print(qc_obj.is_empty())
    # qc_obj.to_base(1)
    # qc_obj.to_base(2)
    # qc_obj.to_base(3)
    # qc_obj.solved()
    # qc_obj.solved()
    # qc_obj.solved()
    # qc_obj.to_base(4)
    # qc_obj.to_base(5)
    # qc_obj.to_base(6)
    # qc_obj.from_base()
    # qc_obj.finalization()
    # qc_obj.finalization()
    # qc_obj.size()