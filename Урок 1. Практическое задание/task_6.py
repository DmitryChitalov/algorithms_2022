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
        self.tacks = []
        self.checking = []
        self.completed = []

    def add_task(self, task):
        self.tacks.insert(0, task)

    def pop_task(self):
        if len(self.tacks) == 0:
            return None
        else:
            return self.tacks.pop()

    def for_checking(self, task):
        self.checking.insert(0, task)

    def add_completed(self, task):
        self.completed.append(task)

    def pop_checking(self):
        if len(self.checking) == 0:
            return None
        else:
            return self.checking.pop()


tb = TaskBoard()
print(tb.tacks)

# 1. Новые задания
n = 16  # сколько заданий добавить
i = 1
while i < n + 1:
    tb.add_task(i)
    i += 3
print(f' Задания {tb.tacks}\n Доработка {tb.checking}\n Выполнено {tb.completed}\n')


# 2.  Внешняя функция для обработки заданий
def work(to_do):
    '''
    если задание выполено заполняется self.completed = [(задание, результат, отметка проверки)]
    если задание не выполнено заполняется self.for_checking = [(задание, отметка проверки)]
    :param to_do:
    :return:
    '''
    if to_do % 2 == 0:
        return tb.add_completed((to_do, to_do / 2, True))
    else:
        return tb.for_checking((to_do, False))


# 3.  Запуск выполнения задания
while len(tb.tacks) != 0:
    work(tb.pop_task())
print(f' Задания {tb.tacks}\n Доработка {tb.checking}\n Выполнено {tb.completed}\n')


# 4.  Запуск доработки из checking
while len(tb.checking) != 0:
    x = tb.pop_checking()
    y = x[0] + 1
    work(y)
print(f' Задания {tb.tacks}\n Доработка {tb.checking}\n Выполнено {tb.completed}\n')
