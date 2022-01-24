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

    def remove(self, other, item):
        other.elems.insert(0, item.from_queue())
        self.elems.pop()


if __name__ == '__main__':
    basic_tasks = QueueClass()
    rev_tasks = QueueClass()
    print(basic_tasks.is_empty())  # -> True. Основная очередь пустая

    # помещаем объекты в основную очередь
    basic_tasks.to_queue('first')
    basic_tasks.to_queue('second')
    basic_tasks.to_queue('third')

    print(basic_tasks.is_empty())  # -> False. Основная очередь не пустая

    print(rev_tasks.is_empty())  # -> True. Очередь для доработки пустая

    print(basic_tasks.size())  # -> 3

    # Переносим задачу в список задач на доработку
    basic_tasks.remove(rev_tasks, basic_tasks)

    print(basic_tasks.size())  # -> 2

    print(rev_tasks.size())    # -> 1

    print(basic_tasks.from_queue())  # -> second

    print(basic_tasks.size())  # -> 1

    print(rev_tasks.from_queue())  # -> first

    print(rev_tasks.size())  # -> 0