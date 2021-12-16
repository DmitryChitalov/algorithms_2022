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


class Task_board:
    def __init__(self):
        self.todo = []
        self.rework = []
        self.done = []

    def is_empty_all(self):
        return self.todo == [] and self.rework == [] and self.done == []

    def is_empty_todo(self):
        return self.todo == []

    def is_empty_rework(self):
        return self.rework == []

    def add_todo(self, item):
        self.todo.insert(0, item)

    def add_rework(self, item):
        self.rework.insert(0, item)

    def add_done(self, item):
        self.done.insert(0, item)

    def todo_to_rework(self):
        if not self.is_empty_todo():
            task = self.todo.pop()
            print('Moving task \'%s\' todo -> rework' % task)
            self.add_rework(task)
        else:
            print('Trying to move task todo -> rework.  No tasks allowed')

    def todo_to_done(self):
        if not self.is_empty_todo():
            task = self.todo.pop()
            print('Moving task \'%s\' todo -> done' % task)
            self.add_done(task)
        else:
            print('No tasks allowed')

    def rework_to_done(self):
        if not self.is_empty_rework():
            task = self.rework.pop()
            print('Moving task \'%s\' rework -> done' % task)
            self.add_done(task)
        else:
            print('Trying to move task rework -> done.  No tasks allowed')


if __name__ == '__main__':
    my_board = Task_board()
    print(my_board.is_empty_all())

    tasks = ['homework', 'washing the car', 'cooking', 'gaming', 'sleeping']

    for i in tasks:
        my_board.add_todo(i)

    print(my_board.todo, my_board.rework, my_board.done)
    my_board.rework_to_done()
    my_board.todo_to_done()
    my_board.todo_to_rework()
    print('to do : %s , rework: %s , done: %s' % (my_board.todo, my_board.rework, my_board.done))
