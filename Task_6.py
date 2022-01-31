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


class Queue:

    def __init__(self):
        self.__data = []
        self.solved = []
        self.revision = []

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        return None

    def to_solved(self):
        self.solved.append(self.dequeue())

    def to_revision(self):
        self.revision.append(self.dequeue())

    def return_from_revision_to_base(self):
        self.enqueue(self.revision.pop(0))

    def rear(self):  # peek
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        return None

    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        return None

    def is_emmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def clear(self):
        self.__data = []

    def __repr__(self):
        array = [str(val) for val in self.__data]
        return ' '.join(array)


q = Queue()
q.enqueue(42)
q.enqueue(33)
q.enqueue(21)
q.enqueue(100)

q.to_solved()
q.to_revision()
q.to_revision()

print(q, q.solved, q.revision)

q.return_from_revision_to_base()
print(q, q.solved, q.revision)