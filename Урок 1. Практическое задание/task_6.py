"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Queue:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.__base = Queue()
        self.__solved = Queue()
        self.__revision = Queue()

    def add_to_base(self, task):
        self.__base.to_queue(task)

    def take_from_base(self):
        return self.__base.from_queue()

    def base_size(self):
        return self.__base.size()

    def base_elems(self):
        return self.__base.elems

    def add_to_solved(self, task):
        self.__solved.to_queue(task)

    def take_from_solved(self):
        return self.__solved.from_queue()

    def solved_size(self):
        return self.__solved.size()

    def solved_elems(self):
        return self.__solved.elems

    def add_to_revision(self, task):
        self.__revision.to_queue(task)

    def take_from_revision(self):
        return self.__revision.from_queue()

    def revision_size(self):
        return self.__revision.size()

    def revision_elems(self):
        return self.__revision.elems


if __name__ == '__main__':
    task_board = TaskBoard()

    def show_tasks():
        print('задач в общем списке: ', task_board.base_size(), ', задачи: ', task_board.base_elems(), sep='')
        print('задач в списке "на доработку": ', task_board.revision_size(), ', задачи: ', task_board.revision_elems(), sep='')
        print('задач в списке решенных: ', task_board.solved_size(), ', зачачи: ', task_board.solved_elems(), sep='')
        print('\n\n')

    print('Добавим на доску десять задач')
    print('=' * 150)
    for n in range(10):
        task_board.add_to_base(f'task{n}')
    show_tasks()

    print('Взяли задачи, порешали, какие решили, какие нет')
    print('=' * 150)
    for i in range(8):
        task = task_board.take_from_base()
        if i in [2, 5, 6]:
            task_board.add_to_revision(task)
        else:
            task_board.add_to_solved(task)
    show_tasks()

    print('Подумали, придумали как решить нерешенные задачи')
    print('=' * 150)
    for i in range(task_board.revision_size()):
        task = task_board.take_from_revision()
        task_board.add_to_solved(task)
    show_tasks()
