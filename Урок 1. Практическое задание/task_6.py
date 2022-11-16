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

from random import randint


class QueueClass:
    def __init__(self):
        self.basic = []
        self.beta = []
        self.solved = []

    def is_empty(self):
        return self.basic == [] and self.beta == [] and self.solved == []

    # Inserting and moving tasks
    def to_basic(self, item):
        self.basic.insert(0, item)

    def from_basic_to_beta(self):
        self.beta.insert(0, self.basic.pop())

    def from_basic_to_solved(self):
        self.solved.insert(0, self.basic.pop())

    def from_beta_to_solved(self):
        self.solved.insert(0, self.beta.pop())

    def size(self):
        return len(self.basic) + len(self.beta) + len(self.solved)

    def view_all_elements(self):
        return f'\nbasic: {qc_obj.basic}\nbeta: {qc_obj.beta}\nsolved: {qc_obj.solved}\nsize: {qc_obj.size()}\n'


if __name__ == '__main__':
    qc_obj = QueueClass()

    tasks_count = randint(10, 15)

    # to_basic
    for i in range(tasks_count):
        qc_obj.to_basic(f'Task {i + 1}')

    print(qc_obj.view_all_elements())

    # from_basic_to_beta
    for i in range(randint(1, 5)):
        qc_obj.from_basic_to_beta()
    print(qc_obj.view_all_elements())

    # from_beta_to_solved
    for i in range(1):
        qc_obj.from_beta_to_solved()
    print(qc_obj.view_all_elements())

    # from_basic_to_solved
    for i in range(1, 5):
        qc_obj.from_basic_to_solved()
    print(qc_obj.view_all_elements())
