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


class Tasks:
    """ Класс для тасок """

    def __init__(self):
        self.tasks = [
            [], # backlog
            [], # fix
            []  # solved
        ]

    def add_backlog(self, task_str):
        self.tasks[0].append(task_str)

    def backlog_move_fix(self, task_str):
        self.__move_task(task_str, 0, 1)

    def move_solve(self, task_str):
        if self.__move_task(task_str, 1, 2) is False:
            self.__move_task(task_str, 0, 2)

    @staticmethod
    def task_type(_type: str):
        if _type == 'backlog':
            return 0
        if _type == 'fix':
            return 1
        if _type == 'solve':
            return 2

    def __move_task(self, task_str, task_from, task_to):
        """ Переместить таску из очереди в другую очередь """
        try:
            idx = self.tasks[task_from].index(task_str)
            item = self.tasks[task_from].pop(idx)
            self.tasks[task_to].append(item)
            return True
        except BaseException:
            return False


taska = Tasks()
taska.add_backlog('Задача в беклоге')
taska.add_backlog('Задача в беклоге')
taska.add_backlog('Задача в беклоге')
taska.add_backlog('Задача в беклоге')
print(taska.tasks)
taska.move_solve('Задача в беклоге')
taska.backlog_move_fix('Задача в беклоге')
taska.backlog_move_fix('Задача в беклоге')
print(taska.tasks)
taska.move_solve('Задача в беклоге')
taska.move_solve('Задача в беклоге')
print(taska.tasks)
taska.move_solve('Задача в беклоге')
print(taska.tasks)