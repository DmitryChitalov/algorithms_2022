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
        self.elements = []

    def to_queue(self, item):
        self.elements.insert(0, item)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def __str__(self):
        result = ''
        for element in self.elements[::-1]:
            result += element + '\n'
        return result


class TaskBoard:
    def __init__(self):
        self._tasks = Queue()
        self._in_progress = Queue()
        self._in_approval = Queue()
        self._completed = []
        self._next_task_number = 0

    def add_task(self):
        self._next_task_number += 1
        self._tasks.to_queue(f'task_{self._next_task_number}')

    def take_task(self):
        self._in_progress.to_queue(self._tasks.from_queue())

    def to_approve(self):
        self._in_approval.to_queue(self._in_progress.from_queue())

    def complete_from_progress(self):
        self._completed.append(self._in_progress.from_queue())

    def complete_from_approving(self):
        self._completed.append(self._in_approval.from_queue())

    def __str__(self):
        result = ''

        result += 'ЗАДАЧИ:\n'
        if self._tasks.size() != 0:
            result += str(self._tasks)
        else:
            result += '-пусто-\n'

        result += 'ВЫПОЛНЯЕМЫЕ ЗАДАЧИ:\n'
        if self._in_progress.size() != 0:
            result += str(self._in_progress)
        else:
            result += '-пусто-\n'

        result += 'НА СОГЛАСОВАНИИ РЕШЕНИЯ:\n'
        if self._in_approval.size() != 0:
            result += str(self._in_approval)
        else:
            result += '-пусто-\n'

        result += 'ВЫПОЛНЕННЫЕ ЗАДАЧИ:\n'
        if len(self._completed) != 0:
            for task in self._completed:
                result += task + '\n'
        else:
            result += '-пусто-\n'

        result += '-' * 25
        return result


if __name__ == '__main__':

    board = TaskBoard()

    board.add_task()
    board.add_task()
    board.add_task()
    board.add_task()
    board.add_task()
    board.add_task()
    print(board)

    board.take_task()
    board.take_task()
    print(board)

    board.to_approve()
    board.complete_from_progress()
    board.take_task()
    print(board)

    board.complete_from_progress()
    board.complete_from_approving()
    print(board)
