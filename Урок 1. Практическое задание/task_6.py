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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

def hot_potato(task, num):
    queue_obj = QueueClass()
    for i in task:
        queue_obj.to_queue(i)

    while queue_obj.size() > 1:
        for i in range(num):
            queue_obj.to_queue(queue_obj.from_queue())

        queue_obj.from_queue()

    return queue_obj.from_queue()


print(hot_potato(["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5", "Задача 6"], 7))


# if __name__ == '__main__':
#     qc_obj = QueueClass()
#     print(qc_obj.is_empty())  # -> True. Очередь пустая
#
#     # помещаем объекты в очередь
#     qc_obj.to_queue('my_obj')
#     qc_obj.to_queue(4)
#     qc_obj.to_queue(True)
#
#     print(qc_obj.is_empty())  # -> False. Очередь пустая
#
#     print(qc_obj.size())  # -> 3
#
#     print(qc_obj.from_queue())  # -> my_obj
#
#     print(qc_obj.size())  # -> 2



