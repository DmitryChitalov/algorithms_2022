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



class QueueClass:
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

    def clear(self):
        self.elems = []

    def all_elements(self):
        return self.elems




class Task_board(QueueClass):
    def __init__(self, tasks):
        self.main_queue = QueueClass()
        self.complete_queue = QueueClass()
        self.uncomplete_queue = QueueClass()
        self.fill_main_queue(tasks)

    def fill_main_queue(self, tasks):
        for task in tasks:
            self.main_queue.to_queue(task)


    def solving_tasks(self):
        '''решение входящих задач'''
        while not self.main_queue.is_empty():
            task = self.main_queue.from_queue()
            if task:
                self.complete_queue.to_queue(task)
            else:
                self.uncomplete_queue.to_queue(task)

    def sloving_uncomplete_tasks(self):
        '''решение не решенных задач'''
        temp = []
        for _ in self.uncomplete_queue:
            temp.append(f'task is over')
        self.uncomplete_queue.clear()
        for _ in temp:
            self.complete_queue.to_queue(task)



    def pirnter_tasks(self):
        print(f'все вновь поступившие не обработанные задачи {self.main_queue.all_elements()}')
        print(f'все завершенные задачи {self.complete_queue.all_elements()}')
        print(f'все задачи на доработку {self.uncomplete_queue.all_elements()}')


Tb = Task_board([True, False, 'test'])
Tb.pirnter_tasks()
print('-'*30)
Tb.solving_tasks()
Tb.pirnter_tasks()
print('*'*30)
