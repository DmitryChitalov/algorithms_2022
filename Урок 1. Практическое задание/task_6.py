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
        self.basic = []
        self.revision = []
        self.solved = []

    def is_empty_basic(self):
        return self.basic == []

    def is_empty_revision(self):
        return self.revision == []

    def is_empty_solved(self):
        return self.solved == []

    def to_basic_queue(self, item):
        self.basic.insert(0, item)

    def from_basic_queue(self):
        return self.basic[-1]

    def from_basic_to_revision_queue(self):
        self.revision.insert(0, self.basic.pop())

    def from_basic_to_solved_queue(self):
        self.solved.insert(0, self.basic.pop())

    def from_revision_queue(self):
        return self.revision[-1]

    def from_revision_to_solved_queue(self):
        self.solved.insert(0, self.revision.pop())

    def size_basic(self):
        return len(self.basic)

    def size_revision(self):
        return len(self.revision)

    def size_solved(self):
        return len(self.solved)


if __name__ == '__main__':
    tb_obj = TaskBoard()
    print(tb_obj.is_empty_basic())  # -> True. "Базовая" очередь пустая
    print(tb_obj.is_empty_revision())  # -> True. "На доработку" очередь пустая
    print(tb_obj.is_empty_solved())  # -> True. "Решенные" очередь пустая

    # помещаем объекты в базовую очередь
    tb_obj.to_basic_queue('task_1')
    tb_obj.to_basic_queue('task_2')
    tb_obj.to_basic_queue('task_3')

    print(tb_obj.is_empty_basic())  # -> False. Очередь не пустая

    print(tb_obj.size_basic())  # -> 3

    print(tb_obj.from_basic_queue())  # -> берём задачу task_1

    tb_obj.from_basic_to_solved_queue()  # отправляем task_1 в решенные

    print(tb_obj.is_empty_solved())  # -> False. Очередь не пустая

    print(tb_obj.from_basic_queue())  # -> берём задачу task_2

    tb_obj.from_basic_to_revision_queue()  # отправляем task_2 на доработку

    print(tb_obj.is_empty_revision())  # -> False. "На доработку" очередь не пустая

    print(tb_obj.from_revision_queue())  # берём задачу task_2

    tb_obj.from_revision_to_solved_queue()  # отправляем task_2 в решенные

    print(tb_obj.is_empty_revision())  # -> True. "На доработку" очередь пустая

    print(tb_obj.is_empty_solved())  # -> False. "Решенные" очередь не пустая
