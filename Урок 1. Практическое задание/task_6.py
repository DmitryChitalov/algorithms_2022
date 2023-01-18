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
class QueueClass:
    def __init__(self):
        self.elems = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def solved_lst(self):
        self.solved.insert(0, self.elems.pop())

    def revision_lst(self):
        self.revision.insert(0, self.elems.pop())

    def solved_task(self):
        self.elems.insert(0, self.revision.pop())


#if __name__ == '__main__':
qc_obj = QueueClass()

qc_obj.to_queue('123')
qc_obj.to_queue(5)
qc_obj.to_queue(True)

print(qc_obj.elems)
qc_obj.solved_lst()
print(qc_obj.solved)
qc_obj.revision_lst()
print(qc_obj.elems)
print(qc_obj.revision)
qc_obj.solved_task()
print(qc_obj.revision)
print(qc_obj.elems)








