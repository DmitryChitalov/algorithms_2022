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
from collections import deque
import random


class Task_board():
    def __init__(self):
        self.main_deque = deque()        # или []
        self.complete_deque = deque()
        self.uncomplete_deque = deque()

    def append_tasks(self, li):
        '''append new task in deque'''
        self.main_deque.extend(li)

    def solving_tasks(self):
        '''решение входящих задач'''
        while len(self.main_deque) > 0:
            task = self.main_deque.pop()
            if task:
                self.complete_deque.append(task)
            else:
                self.uncomplete_deque.append(task)

    def sloving_uncomplete_tasks(self):
        '''попытка решить не решенные задачи'''
        print('попытка решить задачи')
        temp = []
        for _ in self.uncomplete_deque:
            sys_random = random.SystemRandom()
            task = sys_random.choice([True, False])
            temp.append(task)
        self.uncomplete_deque.clear()

        for _ in temp:
            if task:
                self.complete_deque.append(task)
            else:
                self.uncomplete_deque.append(task)


    def pirnter_tasks(self):
        print(f'все вновь поступившие не обработанные задачи {self.main_deque}')
        print(f'все завершенные задачи {self.complete_deque}')
        print(f'все задачи на доработку {self.uncomplete_deque}')


Tb = Task_board()
Tb.append_tasks([True, False, True, True, False, True, True, False, True, True])
Tb.pirnter_tasks()
print('-'*30)
Tb.solving_tasks()
Tb.pirnter_tasks()
print('*'*30)
Tb.sloving_uncomplete_tasks()
Tb.pirnter_tasks()
