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


class Queue:
    def __init__(self):
        self.tasks = []
    def __str__(self):
        return str(self.tasks)

    def add_to(self, tasks):
        #tasks.reverse()
        for i in range(len(tasks)):
            self.tasks.insert(0, tasks[i])

    def remove_from(self, number_of_tasks):
        removed_tasks = []
        for i in range(number_of_tasks):
            if self.tasks == []:
                print('Unable to remove from queue. Queue is empty')
            else:
                removed_tasks.append(self.tasks.pop())
        #removed_tasks.reverse()
        return removed_tasks



class Board():
    def __init__(self):
        self.base_queue = Queue()
        self.edit_queue = Queue()
        self.solved = Queue()

    def to_base(self, tasks): # принимает список задач
        self.base_queue.add_to(tasks)

    def to_edit(self, number_of_tasks):
        self.edit_queue.add_to(self.base_queue.remove_from(number_of_tasks))

    def from_edit(self, number_of_tasks):
        self.base_queue.add_to(self.edit_queue.remove_from(number_of_tasks))

    def to_solved(self, number_of_tasks, from_):
        if from_ == 'base':
            self.solved.add_to(self.base_queue.remove_from(number_of_tasks))
        elif from_ == 'edit':
            self.solved.add_to(self.edit_queue.remove_from(number_of_tasks))
        else:
            print('Please, specify the queue from which you want to move tasks to Solved')

board1 = Board()

# queue1 = Queue()
# print(queue1)
# queue1.add_to(['Homework'])
# print(queue1)
# print(queue1.remove_from(2))
#
# print(queue1)
#
# queue1.add_to(['Homework', 'Classwork', 'Preparation'])
# print(queue1)
# print(queue1.remove_from(2))
#
# print(queue1)

board1.to_base(['task1', 'task2', 'task3', 'task4'])
print(board1.base_queue)
board1.to_solved(2, 'base')
print(board1.base_queue)
print(board1.solved)


