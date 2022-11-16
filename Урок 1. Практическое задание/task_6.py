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

class QueueTasksBoardClass:
    def __init__(self):
        self.basetsk = []
        self.reworktsk = []
        self.done = []

    def is_empty(self):
        return self.basetsk == [], self.reworktsk == [], self.done == []

    def new_tsk(self, item):
        self.basetsk.insert(0, item)

    def to_rework(self):
        self.reworktsk.insert(0,  self.basetsk[-1])
        return self.basetsk.pop()

    def from_base_to_done(self):
        self.done.insert(0, self.basetsk[-1])
        return self.basetsk.pop()

    def from_rework_to_done(self):
        self.done.insert(0, self.reworktsk[-1])
        return self.reworktsk.pop()

    def del_from_done(self):
        return self.done.pop()

    def size(self, queue):
        if queue == 'base':
            return len(self.basetsk)
        elif queue == 'rework':
            return len(self.reworktsk)
        elif queue == 'done':
            return len(self.done)
        else:
            return 'Error'


if __name__ == '__main__':

    QTBC = QueueTasksBoardClass()
    print(QTBC.is_empty()) 

    QTBC.new_tsk('1')
    QTBC.new_tsk('2')
    QTBC.new_tsk('3')
    QTBC.new_tsk('4')
    QTBC.new_tsk('5')
    QTBC.new_tsk('6')
    QTBC.new_tsk('7')

    QTBC.to_rework()

    QTBC.from_base_to_done()

    QTBC.to_rework()

    QTBC.from_base_to_done()

    QTBC.from_rework_to_done()

    QTBC.del_from_done()

    print(QTBC.basetsk, ' Задач в беклоге: ', QTBC.size('base'))
    print(QTBC.reworktsk, ' На доработку: ', QTBC.size('rework'))
    print(QTBC.done, ' Реализовано: ', QTBC.size('done'))