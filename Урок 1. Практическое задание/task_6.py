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


class QueueClass:


    def __init__(self):
        self.intended_goal = []  # поставленные задачи
        self.complete = []  #  задачи на доработку
        self.solved = []  #  выполненные задачи


    def is_empty(self):
        return f" Поставленные задачи: {self.intended_goal}" \
               f" Задачи на доработку: {self.complete}"  \
               f" Выполненные задачи: {self.solved}"

    def to_queue(self, item ):
        self.intended_goal.insert(0, item)  #  ставим задачу в очередь

    def from_queue(self):
        return self.intended_goal.pop()

    def to_complete(self):
        self.complete.insert(0, self.from_queue()) # добавляем задачу на доработку

    def from_complete(self):

        return  self.complete.pop() # удаляем задачу из доработанных

    def to_solved(self):
        self.solved.insert(0, self.from_queue())  # добавляем в выполненные задачи обработанную

    def post_completion_task(self):
        self.solved.insert(0, self.from_complete())  # добавляем в выполненные задачи доработанную
    # def size(self):
    #     return len(self.intended_goal)


if __name__ == '__main__':

    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # --> Поставленные задачи: [] Задачи на доработку: [] Выполненные задачи: []

    # помещаем объекты в очередь
    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)


    print(qc_obj.is_empty())  # --> Поставленные задачи: [True, 4, 'my_obj'] Задачи на доработку: [] Выполненные задачи: []
    qc_obj.to_complete()  # добавляем задачу на доработку
    print(qc_obj.is_empty())
    qc_obj.to_solved()   #  поставленная задача --> выполнена
    print(qc_obj.is_empty())
    qc_obj.post_completion_task()  # доработанная задача --> выполнена
    print(qc_obj.is_empty())
    qc_obj.to_complete()
    print(qc_obj.is_empty())
    qc_obj.post_completion_task()
    print(qc_obj.is_empty())

# -->  Поставленные задачи: [] Задачи на доработку: [] Выполненные задачи: []
# --> Поставленные задачи: [True, 4, 'my_obj'] Задачи на доработку: [] Выполненные задачи: []
# --> Поставленные задачи: [True, 4] Задачи на доработку: ['my_obj'] Выполненные задачи: []
# --> Поставленные задачи: [True] Задачи на доработку: ['my_obj'] Выполненные задачи: [4]
# --> Поставленные задачи: [True] Задачи на доработку: [] Выполненные задачи: ['my_obj', 4]
# --> Поставленные задачи: [] Задачи на доработку: [True] Выполненные задачи: ['my_obj', 4]
# --> Поставленные задачи: [] Задачи на доработку: [] Выполненные задачи: [True, 'my_obj', 4]


# def hot_potato(names_lst, num):
#     queue_obj = QueueClass()
#     for name in names_lst:
#         queue_obj.to_queue(name)
#
#     while queue_obj.size() > 1:
#         for i in range(num):
#             queue_obj.to_queue(queue_obj.from_queue())
#
#         queue_obj.from_queue()
#
#     return queue_obj.from_queue()
#
#
# print(hot_potato(["Вася", "Петя", "Света", "Жанна", "Катя", "Лена"], 8))
