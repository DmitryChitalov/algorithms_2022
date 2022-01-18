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

class QueueClass:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []


    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_from_revision_to_base(self):
        self.base.insert(0, self.revision.pop())

    def return_from_revision_to_solved(self):
        self.solved.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    qc_obj = QueueClass()

    qc_obj.to_queue('first_obj')
    qc_obj.to_queue('second_obj')
    qc_obj.to_queue('third_obj')

    print(qc_obj.base)  #база
    qc_obj.to_solved() #перенос задачи из базы в решенные
    print(qc_obj.solved) #очередь решенных задач (добавилась первая задача)
    qc_obj.to_revision() #перенос задачи из базы на доработку
    print(qc_obj.base) #база - осталась только третья задача
    print(qc_obj.revision) #очередь на доработку (добавилась задача2)
    qc_obj.return_from_revision_to_base() #перенос задачи из доработки в базу
    print(qc_obj.revision)  #из доработки задача вернулась в базу
    qc_obj.to_revision() #перенос задачи из базы сноыва на доработку
    qc_obj.return_from_revision_to_solved() #перенос задачи из доработки в базу решенных
    print(qc_obj.solved) #очередь решенных задач
    print(qc_obj.base) #база