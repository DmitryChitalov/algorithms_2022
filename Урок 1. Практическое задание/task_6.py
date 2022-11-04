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

# from task_5 import StackClass
from random import randint


class Queue:
    """Класс базовой очереди"""
    def __init__(self):
        self.elements = list()

    def push(self, item):
        self.elements.insert(0, item)

    def pull(self):
        return self.elements.pop()

    @staticmethod
    def is_correct():
        return round(randint(0, 1))


class ModifyQueue(Queue):
    """Класс очереди на доработку"""
    def __init__(self):
        super(ModifyQueue, self).__init__()
        self.elements = list()

    def pull(self):
        """Метод pull класса-наследника отличается тем, что в случае если результат проверки
        отрицательный, работа возвращается на доработку"""
        checked_paper = self.elements.pop()
        if Queue.is_correct() == 0:
            self.push(checked_paper)
        return checked_paper


queue = Queue()
modify_queue = ModifyQueue()
checked = Queue()

queue.push("Домашнее задание №1")
queue.push("Домашнее задание №2")
queue.push("Домашнее задание №3")
print(queue.elements)
print(modify_queue.elements)
print(f'{checked.elements}\n')
paper = queue.pull()
print(f'Домашнее задание на проверку: {paper}\n')
if Queue.is_correct() == 0:
    modify_queue.push(paper)
else:
    checked.push(paper)
print(queue.elements)
print(modify_queue.elements)
print(f'{checked.elements}\n')
if len(modify_queue.elements) > 0:
    paper = modify_queue.pull()
    print(f'Домашнее задание на перепроверку: {paper}\n')
    if Queue.is_correct() == 1:
        checked.push(paper)
    print(queue.elements)
    print(modify_queue.elements)
    print(checked.elements)