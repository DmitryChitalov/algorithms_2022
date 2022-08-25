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

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        print('Added an element')
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskQueue(QueueClass):
    def from_queue(self):
        print('Solved the problem')
        el = self.elems.pop()
        spc_obj.to_queue(el)
        return el

    def from_revision(self):
        print('Need revision')
        el = self.elems.pop()
        rc_obj.to_queue(el)
        return el


class SolvedProblems(QueueClass):
    def __init__(self):
        self.elems = []


class Revision(QueueClass):
    def __init__(self):
        self.elems = []

if __name__ == '__main__':
    qc_obj = QueueClass()
    tc_obj = TaskQueue()
    spc_obj = SolvedProblems()
    rc_obj = Revision()
    print('TaskQueue is empty: ', tc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    tc_obj.to_queue('Task_1')
    tc_obj.to_queue('Task_2')
    tc_obj.to_queue('Task_3')
    tc_obj.to_queue('Task_4')
    tc_obj.to_queue('Task_5')
    tc_obj.to_queue('Task_6')
    tc_obj.to_queue('Task_7')
    tc_obj.to_queue('Task_8')
    tc_obj.to_queue('Task_9')


    print('TaskQueue is empty: ', tc_obj.is_empty())  # -> False. Очередь пустая

    print('TaskQueue length: ', tc_obj.size())  # -> 9


    print('SolvedProblems is empty: ', spc_obj.is_empty())  # -> True. Очередь пустая

    print(tc_obj.from_queue())  # -> 'Task_1'

    print('TaskQueue length: ', tc_obj.size())  # -> 8
    print('SolvedProblems is empty: ', spc_obj.is_empty())  # -> False. Очередь пустая
    print('SolvedProblems: ', spc_obj.size())  # -> 1


    print('TaskQueue length: ', tc_obj.size())  # -> 8
    print('Revision is empty: ', rc_obj.is_empty())  # -> True. Очередь пустая

    print(tc_obj.from_revision())  # -> 'Task_2'

    print('TaskQueue length: ', tc_obj.size())  # -> 7
    print('Revision is empty: ', rc_obj.is_empty())  # -> False. Очередь пустая
    print('Revision: ', rc_obj.size())  # -> 1