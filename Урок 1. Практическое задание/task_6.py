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


class TaskBoardClass:
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
    TBC_homeworks = TaskBoardClass()
    print(TBC_homeworks.to_queue('выбросить мусор'))
    print(TBC_homeworks.to_queue('полить деревья'))
    print(TBC_homeworks.to_queue('поиграть с детьми'))
    print(TBC_homeworks.to_queue('наладить самокат'))
    print(TBC_homeworks.is_empty())
    print(TBC_homeworks.size())
    print(TBC_homeworks.from_queue('todo'))
    print(TBC_homeworks.from_queue('todo'))
    print(TBC_homeworks.from_queue('todo'))
    print(TBC_homeworks.to_rework())
    print(TBC_homeworks.size())
    print(TBC_homeworks.from_queue('rework'))
    print(TBC_homeworks.size())
