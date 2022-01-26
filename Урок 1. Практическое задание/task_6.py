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


class TaskBoard:
    def __init__(self):
        self.base = []
        self.unsolved = []
        self.solved = []
        self.graveyard = []  # заброшенные

    def is_empty(self, q):
        if q == 'base':
            return self.base == []
        elif q == 'unsolved':
            return self.unsolved == []
        elif q == 'solved':
            return self.solved == []
        elif q == 'graveyard':
            return self.graveyard == []
        else:
            return 'You must choose a task queue name'

    def to_base(self, item):
        self.base.insert(0, item)

    def from_q_to_q(self, from_q, to):
        if from_q == 'base':
            if len(self.base) < 1:
                print('Base task board is empty')
            elif to == 'unsolved':
                self.unsolved.insert(0, self.base.pop())
            elif to == 'solved':
                self.solved.insert(0, self.base.pop())
            else:
                print('You must choose a task queue name')
        elif from_q == 'unsolved':
            if len(self.unsolved) < 1:
                print('Unsolved task board is empty')
            elif to == 'solved':
                self.solved.insert(0, self.unsolved.pop())
            elif to == 'graveyard':
                self.graveyard.insert(0, self.unsolved.pop())
            else:
                print('You must choose a task queue name')
        else:
            print('You must choose a task queue name')

    def size(self, of):
        if of == 'base':
            return len(self.base)
        elif of == 'unsolved':
            return len(self.unsolved)
        elif of == 'solved':
            return len(self.solved)
        elif of == 'graveyard':
            return len(self.graveyard)
        else:
            return 'You must choose a task queue name'


if __name__ == '__main__':
    qc_obj = TaskBoard()

    print(qc_obj.is_empty('base'))
    print(qc_obj.is_empty('solved'))
    print(qc_obj.is_empty('asd'))

    qc_obj.to_base('math')
    qc_obj.to_base('program')
    qc_obj.to_base('pycharm')
    qc_obj.to_base('client')
    qc_obj.to_base('sql')
    qc_obj.to_base('database')
    qc_obj.to_base('server')
    qc_obj.to_base('software')
    qc_obj.to_base('hardware')

    print(qc_obj.is_empty('base'))

    print(qc_obj.base)

    print(qc_obj.size('base'))

    qc_obj.from_q_to_q('base', 'solved')
    qc_obj.from_q_to_q('unsolved', 'solved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('unsolved', 'solved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('unsolved', 'graveyard')
    qc_obj.from_q_to_q('base', 'solved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('base', 'solved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('base', 'unsolved')
    qc_obj.from_q_to_q('base', 'solved')

    print(qc_obj.size('base'))
    print(qc_obj.size('solved'))
    print(qc_obj.size('unsolved'))
    print(qc_obj.size('graveyard'))

    print(qc_obj.base)
    print(qc_obj.solved)
    print(qc_obj.unsolved)
    print(qc_obj.graveyard)
