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

from heapq import heappush, heappop


class TaskBoardClass():
    DICT_QUEUE = {1: 'basic', 2: 'mod', 3: 'comp'}
    DIMENSION_BOARD = 10 ** 9
    task_number = 0

    def __init__(self):
        self.basic = []
        self.mod = []
        self.comp = []

    # добавление задачи (1-высшая срочность, 2-средняя, 3-низшая)
    def add_task(self, urgency=3):
        TaskBoardClass.task_number += 1
        heappush(self.basic, urgency * TaskBoardClass.DIMENSION_BOARD + TaskBoardClass.task_number)

    # перемещение задачи (1-основная очередь, 2-на доработке, 3-выполненные)
    def update_status(self, status_old, status_new):
        if status_old == 1 and len(self.basic) == 0:
            raise ValueError(f'Список задач пуст')
        elif status_old > status_new:
            raise ValueError(f'Невозможно вернуть задачу в основную очередь или на доработку')
        elif status_old == status_new:
            raise ValueError(f'Статусы не могут быть одинаковыми')
        elif status_old == 2 and len(self.mod) == 0:
            raise ValueError(f'Список доработки пуст')
        else:
            task = heappop(eval(f'self.{TaskBoardClass.DICT_QUEUE[status_old]}'))
            heappush(eval(f'self.{TaskBoardClass.DICT_QUEUE[status_new]}'), task)

    def __str__(self):
        return f'Основная: {self.basic}\nНа доработке: {self.mod}\nВыполненные: {self.comp}'

