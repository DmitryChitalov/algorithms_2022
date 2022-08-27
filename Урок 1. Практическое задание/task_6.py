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


class TaskBoard:
    def __init__(self):
        self.todo = []
        self.done = []
        self.rework = []
        print('создана новая доска')

    def is_empty(self):
        return self.todo == []

    def to_queue(self, item):
        self.todo.insert(0, item)
        return f'Список задач обновлён:: {self.todo}'

    def from_queue(self, queue):
        if queue == 'todo':
            self.done.insert(0, self.todo.pop())
        if queue == 'rework':
            self.done.insert(0, self.rework.pop())
        return f'Список выполненных задач обновлён: {self.done}'

    def to_rework(self):
        self.rework.insert(0, self.todo.pop())
        return f'Список задач на доработку обновлён: {self.rework}'

    def size(self):
        return f'Задач в работе: {len(self.todo) + len(self.rework)}'


if __name__ == '__main__':
    tb_homework = TaskBoard()
    print(tb_homework.to_queue('выбросить мусор'))
    print(tb_homework.to_queue('полить деревья'))
    print(tb_homework.to_queue('поиграть с детьми'))
    print(tb_homework.to_queue('наладить самокат'))
    print(tb_homework.is_empty())
    print(tb_homework.size())
    print(tb_homework.from_queue('todo'))
    print(tb_homework.from_queue('todo'))
    print(tb_homework.from_queue('todo'))
    print(tb_homework.to_rework())
    print(tb_homework.size())
    print(tb_homework.from_queue('rework'))
    print(tb_homework.size())