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


class MyQueue:
    def __init__(self):
        self.queue_list = [[], [], []]

    def add(self, new_task):
        self.queue_list[0].insert(0, new_task)

    def to_solved(self):
        if len(self.queue_list[0]) != 0:
            solved_task = self.queue_list[0].pop()
            self.queue_list[1].insert(0, solved_task)
        else:
            print('Очередь пуста!')

    def to_revision(self):
        if len(self.queue_list[0]) != 0:
            revision_task = self.queue_list[0].pop()
            self.queue_list[2].insert(0, revision_task)
        else:
            print('Очередь пуста!')

    def size(self):
        print(f"Задач в общей очереди: " + str(len(self.queue_list[0])))
        print(f"Задач выполненных: " + str(len(self.queue_list[1])))
        print(f"Задач на доработку: " + str(len(self.queue_list[2])))

    def print_queues(self):
        print(self.queue_list)


new_queue = MyQueue()

new_queue.add(12355)
new_queue.add(12356)
new_queue.add(12357)
new_queue.add(12358)
new_queue.to_solved()
new_queue.to_revision()
new_queue.to_revision()
new_queue.to_revision()
new_queue.to_revision()
new_queue.print_queues()
new_queue.add(12359)
new_queue.add(12360)
new_queue.size()
new_queue.print_queues()
