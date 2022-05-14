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
        self.unsolved = []
        self.revision = []
        self.solved = []

    def to_queue(self, item):
        self.unsolved.insert(0, item)

    def base_queue(self):
        inp = input(f'Отправить задачу {self.unsolved[-1]} на доработку? Если да, нажмите "y".'
                    'Иначе нажмите любую другую клавишу и задача будет выполнена. ')
        if inp.lower() == 'y':
            self.revision.insert(0, self.unsolved.pop())
        else:
            self.solved.append(self.unsolved.pop())

    def revision_queue(self):
        self.solved.append(self.revision.pop())

    def solved_task(self):
        return self.solved

    def unsolved_task(self):
        return self.unsolved

    def revision_task(self):
        return self.revision


if __name__ == '__main__':
    tb = TaskBoard()

    for task in range(1, 10):
        tb.to_queue(f'Задача {task}. №:{task}')

    print(tb.unsolved_task())
    tb.base_queue()
    print(tb.unsolved_task())
    tb.base_queue()
    tb.revision_queue()
    print(tb.solved_task())
