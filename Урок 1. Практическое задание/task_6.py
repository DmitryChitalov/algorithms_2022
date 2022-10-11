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


class Board:
    def __init__(self):
        self.base_queue = []
        self.for_revision = []
        self.archive = []

    def clear_board(self):
        self.base_queue = []
        self.for_revision = []
        self.archive = []

    def new_task(self, task):
        self.base_queue.insert(0, task)

    def from_base(self):
        return self.base_queue.pop()

    def from_revision(self):
        return self.for_revision.pop()

    def to_revision(self):
        self.for_revision.insert(0, self.from_base())

    def to_archive_from_revision(self):
        self.archive.append(self.from_revision())

    def to_archive_from_base(self):
        self.archive.append(self.from_base())

    def show_bq(self):
        bq_str = f'base queue: {", ".join(self.base_queue)}'
        return bq_str

    def show_rev(self):
        rev_str = f'for_revision: {", ".join(self.for_revision)}'
        return rev_str

    def show_archive(self):
        archive_str = f'archive: {", ".join(self.archive)}'
        return archive_str

    def __str__(self):
        return self.show_bq() + '\n' + self.show_rev() + '\n' + self.show_archive()


if __name__ == '__main__':
    my_board = Board()
    for i in range(1, 11):
        my_board.new_task(f'task {i}')
    my_board.to_revision()
    my_board.to_archive_from_base()
    my_board.to_revision()
    my_board.to_archive_from_revision()
    print(my_board)
