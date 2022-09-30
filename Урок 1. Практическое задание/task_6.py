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


class Task_Board:
    def __init__(self):
        self.tasks = []
        self.problems = []
        self.done = []

    def __str__(self):
        return (f' tasks {self.tasks} problems {self.problems} done {self.done}')

    def is_empty(self, degue):
        return degue == []

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue(self, degue):
        return degue.pop()

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue_to_queue(self, fr, to):
        item = fr.pop()
        to.insert(0, item)

    def size(self, degue):
        return len(degue)


if __name__ == '__main__':
    tb = Task_Board()
    print(tb.is_empty(tb.tasks))  # -> True. Очередь пустая

    # помещаем объекты в очередь
    tb.to_queue(tb.tasks, 1)
    tb.to_queue(tb.tasks, 2)
    tb.to_queue(tb.tasks, 3)
    print(tb)

    tb.from_queue_to_queue(tb.tasks, tb.problems)
    tb.from_queue_to_queue(tb.tasks, tb.done)
    print(tb)

    tb.from_queue(tb.done)
    print(tb)

    print(tb.is_empty(tb.tasks))  # -> False. Очередь пустая
    print(tb.size(tb.tasks))  # -> 3

